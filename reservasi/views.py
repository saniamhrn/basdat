from django.shortcuts import render, redirect, HttpResponse
from utils.query import query

def reservasi(request):
    return render(request, "form_reservasi.html")

def show_reservasi_kamar(request, custemail = 'Crystal_Edwards8371@yfxpw.info'):
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

    return render(request, 'detail_reservasi.html', {'data': data[0]})