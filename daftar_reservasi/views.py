from django.shortcuts import render, redirect, HttpResponse
from utils.query import query

# Create your views here.
def show_daftar_reservasi(request):
    data = query(f""" 
                SELECT RR.rsv_id, RR.rnum, RR.datetime, RS.status, RR.isactive
                FROM RESERVATION_ROOM RR, RESERVATION_STATUS RS
                WHERE RR.rsv_id = RS.id
                ORDER BY rsv_id ASC;
                """)
    print(data)
    context = {
        "data" : data,
    }
    return render(request, "daftar_reservasi.html", context)

def update_status_reservasi(request, rsv_id):
    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        data = query(f"""
                UPDATE RESERVATION_ROOM
                SET isactive = {new_status}
                WHERE rsv_id = '{rsv_id}';
            """) 
        return redirect('daftar_reservasi')
    else:
        data = query(f"""
                SELECT rsv_id, rNum, Datetime, isActive
                FROM RESERVATION_ROOM
                WHERE rsv_id = '{rsv_id}';
            """)
        if not data:
            return HttpResponse("Reservation not found", status=404)

        return render(request, 'update_reservation.html', {'data': data[0]})

def update_pembayaran(request, rsv_id):
    if request.method == 'POST':
        new_status = request.POST.get('new_status')
        print("masuk sinii")
        print(f"New Status: {new_status}")
        data = query(f"""
                UPDATE RESERVATION_STATUS
                SET status = '{new_status}'
                WHERE id = '{rsv_id}';
            """) 
        print(f"SQL Query: {data}")
        return redirect('daftar_reservasi')
    else:
        print("masuk bawahh")
        data = query(f"""
                SELECT id, status
                FROM RESERVATION_STATUS
                WHERE id = '{rsv_id}';
            """)
        if not data:
            return HttpResponse("Reservation not found", status=404)

        return render(request, 'update_pembayaran.html', {'data': data[0]})

def detail_reservation(request, rsv_id):
    # Retrieve the details of the reservation for the specified rsv_id
    data = query(f"""
                SELECT rsv_id, rNum, Datetime, isActive
                FROM RESERVATION_ROOM
                WHERE rsv_id = '{rsv_id}';
            """)
    shuttle = query(f""" 
                SELECT RS.rsv_id, RS.vehicle_num, RS.driver_phonenum, RS.datetime, RS.isactive
                FROM RESERVATION_SHUTTLESERVICE RS
                JOIN RESERVATION_ROOM RR ON RR.rsv_id = RS.rsv_id AND RR.rsv_id = '{rsv_id}'
                """)
    print(data[0])
    print(shuttle[0])
    if not data:
        return HttpResponse("Reservation not found", status=404)

    return render(request, 'detail_reservation.html', {'data': data[0],'shuttle':shuttle[0]})
        