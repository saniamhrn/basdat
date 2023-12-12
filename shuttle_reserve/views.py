from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib import messages
from utils.query import query

# Create your views here.
def reservasi_shuttle(request,rsv_id):
    isactive = query(f"""
                SELECT isactive
                FROM RESERVATION_ROOM
                WHERE rsv_id = '{rsv_id}';
            """) 
    print(isactive[0].isactive)
    if isactive[0].isactive:
        if request.method == 'POST':
            # rsv_id = request.POST.get('rsv_id')
            kendaraan = request.POST.get('kendaraan')
            data = query(f"""
                    UPDATE RESERVATION_SHUTTLESERVICE
                    SET isactive = 'true'
                    WHERE rsv_id = '{rsv_id}';
                """) 
            return redirect('reservasi:daftar_reservasi_kamar')
        else:
            data = query(f"""
                    SELECT rsv_id, vehicle_num, driver_phonenum, datetime, isactive
                    FROM RESERVATION_SHUTTLESERVICE
                    WHERE rsv_id = '{rsv_id}';
                """)
            if not data:
                return HttpResponse("Reservation not found", status=404)
    else:
        # messages.error(request, 'Room reservation is required to make a shuttle reservation.')
        # return HttpResponse("Reservation is not active", status=404)
        return render(request,'error.html')
    
    return render(request, 'shuttle_reserve.html', {'data': data[0]})