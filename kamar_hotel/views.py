from django.shortcuts import render, redirect, HttpResponse
from utils.query import query

def show_room_list(request):
    custemail = 'azul.hotel@gmail.com'

    hotel_data = query(f""" 
        SELECT hotel_name, hotel_branch FROM hotel
        WHERE email = '{custemail}'
    """)

    hotel = hotel_data[0]

    room_data = query(f"""
        SELECT r.hotel_name, r.hotel_branch, r.number, r.price, r.floor
        FROM room r
        WHERE r.hotel_name = '{hotel[0]}' AND r.hotel_branch = '{hotel[1]}'
        ORDER BY hotel_name ASC
    """)

    room_facilities_data = query(f"""
        SELECT rf.hotel_name, rf.rnum, rf.distance
        FROM room_facilities rf
        WHERE rf.hotel_name = '{hotel[0]}' AND rf.hotel_branch = '{hotel[1]}'
    """)

    # Create a dictionary to store room facilities data by room number
    room_facilities_dict = {row[1]: {'distance': row[2]} for row in room_facilities_data}

    data = []
    for row in room_data:
        room_number = row[2]
        room_facilities = room_facilities_dict.get(room_number, {'distance': None})

        data.append({
            'hotel_name': row[0],
            'hotel_branch': row[1],
            'number': row[2],
            'price': row[3],
            'floor': row[4],
            'distance': room_facilities['distance'],
        })

    context = {
        'data': data
    }
    return render(request, "room_list.html", context=context)



def tambah_kamar(request):
    if request.method == 'POST':
        try:
            custemail = 'azul.hotel@gmail.com'

            data = query(f""" 
            SELECT hotel_name, hotel_branch FROM hotel
            WHERE email = '{custemail}' LIMIT 1
            """)

            hotel = data[0]

            hotel_name = hotel[0]
            hotel_branch = hotel[1]
            number = request.POST.get('nokamar')
            price = request.POST.get('harga')
            floor = request.POST.get('lantai')

            insert = query(f"""
                INSERT INTO room (hotel_name, hotel_branch, number, price, floor)
                VALUES ('{hotel_name}', '{hotel_branch}', {number}, {price}, {floor})
            """)

            print(insert)

            return redirect('daftar_kamar')
        except Exception as e:
            return HttpResponse(f"Error: {e}")

    return render(request, "form_tambah_kamar.html")


def tambah_fasilitas_kamar(request):
    return render(request, "form_tambah_fasilitas_kamar.html")


def delete_room(request):
    if request.method == 'POST':
        hotel_name = request.POST.get('hotel_name')
        hotel_branch = request.POST.get('hotel_branch')
        number = request.POST.get('number')

        is_active = query(f"""
            SELECT isactive FROM reservation_room
            WHERE rhotelname = '{hotel_name}' AND rhotelbranch = '{hotel_branch}' AND rnum = '{number}'
        """)

        if is_active and is_active[0]:
            return HttpResponse("Cannot delete an active room.")
        
        try:
            delete = query(f"""
                DELETE FROM room
                WHERE hotel_name = '{hotel_name}' AND hotel_branch = '{hotel_branch}' AND number = '{number}'
            """)

            return redirect('daftar_kamar')
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    else:
        return HttpResponse("Invalid request method.")