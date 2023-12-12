from datetime import datetime
import random
from django.shortcuts import render, redirect, HttpResponse
from utils.query import query

def reservasi(request):
    return render(request, "form_reservasi.html")

def form_reservasi(request):
    def generate_random_string(length):
        random_string = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', k=length))
        return random_string
    
    def generate_payment_id():
        part1 = ''.join(random.choices('0123456789', k=3))
        part2 = ''.join(random.choices('0123456789', k=2))
        part3 = ''.join(random.choices('0123456789', k=4))
        random_string = f"{part1}-{part2}-{part3}"
        return random_string
    
    if request.method == 'POST':
        user_data = request.session['user_data']
        email = user_data['email']

        hotel_name = request.POST.get('hotel_name')
        hotel_branch = request.POST.get('hotel_branch')
        number = request.POST.get('number')

        checkin = request.POST.get('start_date')
        checkout = request.POST.get('end_date')
        payment_option = request.POST.get('payment_option')
        payment = request.POST.get('payment')
        payment_id = generate_payment_id()

        create_payment = query(f"""
        INSERT INTO payment (payment_id, status) VALUES ('{payment_id}', 'pending')
        """)

        payment_query = ""
        if payment_option == 'kredit':
            payment_query += f"""
            INSERT INTO kredit (no_kartu, payment_id) VALUES ('{payment}', '{payment_id}')
            """
        elif payment_option == 'debit':
            payment_query += f"""
            INSERT INTO debit (no_rekening, payment_id) VALUES ('{payment}', '{payment_id}')
            """
        elif payment_option == 'ewallet':
            payment_query += f"""
            INSERT INTO ewallet (phone_num, payment_id) VALUES ('{payment}', '{payment_id}')
            """

        create_payment_method = query(payment_query)

        rid = generate_random_string(20)

        hotel = query(f"""
        SELECT * FROM room WHERE 
        hotel_name = '{hotel_name}' AND 
        hotel_branch = '{hotel_branch}' AND 
        number = '{number}.0'
        """)

        hotel = hotel[0]

        reservation_query = query(f"""
        INSERT INTO reservation (rid, total_price, checkin, checkout, payment, cust_email)
        VALUES('{rid}', '{hotel[3]}', '{checkin}', '{checkout}', '{payment_id}', '{email}')
        """)

        reservation_status_query = query(f"""
        INSERT INTO reservation_status (id, status)
        VALUES('{rid}', 'Menunggu Konfirmasi Pihak Hotel')
        """)

        date = datetime.today().strftime('%Y-%m-%d')

        reservation_room_query = query(f"""
        INSERT INTO reservation_room (rsv_id, rnum, rhotelname, rhotelbranch, datetime, isactive)
        VALUES('{rid}', '{number}.0', '{hotel_name}', '{hotel_branch}', '{date}', 'false')
        """)

        print(reservation_room_query)

        return redirect('reservasi:daftar_reservasi_kamar')
    else:
        return render(request, 'form_reservasi.html')
    
def show_reservasi_kamar(request, custemail = 'Eduardo_Greenwood7181@1kmd3.site'):
    data = query(f""" 
                SELECT rr.rsv_id, rr.rNum, rr.Datetime, rr.isActive
                FROM reservation r
                JOIN reservation_room rr ON r.rID = rr.rsv_id
                WHERE r.cust_email = '{custemail}'
                """)
    context = {
        "data" : data,
    }
    return render(request, "daftar_reservasi_kamar.html", context)

def detail_reservasi(request, rsv_id):
    # Retrieve the details of the reservation for the specified rsv_id
    data = query(f"""
                SELECT rsv_id, rNum, rHotelName, rHotelBranch, Datetime, isActive
                FROM RESERVATION_ROOM
                WHERE rsv_id = '{rsv_id}';
            """)
    shuttle = query(f""" 
                SELECT RS.rsv_id, RS.vehicle_num, RS.driver_phonenum, RS.datetime, RS.isactive
                FROM RESERVATION_SHUTTLESERVICE RS
                JOIN RESERVATION_ROOM RR ON RR.rsv_id = RS.rsv_id AND RR.rsv_id = '{rsv_id}'
                """)
    if not data:
        return HttpResponse("Reservation not found", status=404)

    return render(request, 'detail_reservasi_kamar.html', {'data': data[0],'shuttle':shuttle[0]})

def show_shuttle_reserve(request):
    return render(request, "shuttle_reserve.html")

def cancel_reservasi(request, rsv_id):
    query(f"""
        UPDATE reservation
        SET status = 6
        WHERE rsv_id = '{rsv_id}';
    """)

    return redirect('reservasi:daftar_reservasi_kamar')

def complaint_page(request, rsv_id):
    return render(request, "complaint.html", {'id' : rsv_id})

def save_complaint(request):
    if request.method == 'POST':

        rsv_id = request.POST.get('id')
        complaint_message = request.POST.get('complain')

        try:
            data = query(f""" 
                SELECT rr.rsv_id, r.cust_email, rr.rNum, rr.Datetime, rr.isActive
                FROM reservation r
                JOIN reservation_room rr ON r.rID = rr.rsv_id
                WHERE r.rid = '{rsv_id}'
            """)

            if not data:
                return HttpResponse("Reservation not found", status=404)

            insert = query(f"""
                INSERT INTO complaints
                (cust_email, rv_id, complaint)
                VALUES ('{data[0].cust_email}', '{rsv_id}', '{complaint_message}')
            """)

            print(insert)

            return redirect('reservasi:daftar_reservasi_kamar')

        except Exception as e:
            print("error:", e)
            return HttpResponse(f"An error occurred: {str(e)}", status=500)

    return HttpResponse("Invalid request method")