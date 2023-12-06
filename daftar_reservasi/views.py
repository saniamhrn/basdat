from django.shortcuts import render, redirect, HttpResponse
from utils.query import query

# SELECT * FROM "SISTEL".RESERVATION;
# Create your views here.
def show_daftar_reservasi(request):
    # data = query(f""" 
    #             SELECT *
    #             FROM RESERVATION_ROOM RR
    #             ORDER BY rsv_id ASC;
    #             """)

    data = query(f""" 
                SELECT RR.rsv_id, RR.rnum, RR.datetime, RS.status, RR.isactive
                FROM RESERVATION_ROOM RR, RESERVATION_STATUS RS
                WHERE RR.rsv_id = RS.id
                ORDER BY rsv_id ASC;
                """)
    context = {
        "data" : data,
    }
    return render(request, "daftar_reservasi.html",context)

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
        data = query(f"""
                UPDATE RESERVATION_STATUS
                SET status = {new_status}
                WHERE id = '{rsv_id}';
            """) 
        return redirect('daftar_reservasi')
    else:
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
    if not data:
        return HttpResponse("Reservation not found", status=404)

    return render(request, 'detail_reservation.html', {'data': data[0]})
        

        
    
# def update_reservation(request, rsv_id):
#     if request.method == 'POST':
#         # Get the new status from the form
#         new_status = request.POST.get('new_status')

#         # SQL query to update the reservation status
#         update_sql = f"""
#             UPDATE RESERVATION_ROOM
#             SET isActive = {new_status}
#             WHERE rsv_id = '{rsv_id}';
#         """

#         # Execute the update query
#         execute_query(update_sql)

#         # Redirect to the reservation list after updating
#         return redirect('reservation_list')

#     else:
#         # Retrieve the current reservation data for the form
#         select_sql = f"""
#             SELECT rsv_id, rNum, Datetime, isActive
#             FROM RESERVATION_ROOM
#             WHERE rsv_id = '{rsv_id}';
#         """

#         reservation = execute_query(select_sql)

#         if not reservation:
#             return HttpResponse("Reservation not found", status=404)

#         return render(request, 'update_reservation.html', {'reservation': reservation[0]})