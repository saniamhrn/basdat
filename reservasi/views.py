from django.shortcuts import render, redirect, HttpResponse
from utils.query import query

def reservasi(request):
    return render(request, "form_reservasi.html")


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
    return render(request, "daftar_reservasi_kamar.html",context)

def detail_reservasi(request, rsv_id):
    # Retrieve the details of the reservation for the specified rsv_id
    data = query(f"""
                SELECT rsv_id, rNum, rHotelName, rHotelBranch, Datetime, isActive
                FROM RESERVATION_ROOM
                WHERE rsv_id = '{rsv_id}';
            """)
    if not data:
        return HttpResponse("Reservation not found", status=404)

    return render(request, 'detail_reservasi_kamar.html', {'data': data[0]})

def show_shuttle_reserve(request):
    return render(request, "shuttle_reserve.html")

def cancel_reservasi(request, rsv_id):
    query(f"""
        UPDATE reservation
        SET status = 6
        WHERE rsv_id = '{rsv_id}';
    """)

    return redirect('daftar_reservasi_kamar')

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

            return redirect('daftar_reservasi_kamar')

        except Exception as e:
            print("error:", e)
            return HttpResponse(f"An error occurred: {str(e)}", status=500)

    return HttpResponse("Invalid request method")