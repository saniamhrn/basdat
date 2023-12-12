from django.shortcuts import render, HttpResponse
from utils.query import query

def show_daftar_hotel(request): 
    minPrice = request.GET.get('min')
    maxPrice = request.GET.get('max')
    if minPrice and maxPrice:
        data = query(f"""
                SELECT DISTINCT H.hotel_name, H.rating, H.nib
                FROM ROOM R, HOTEL H
                WHERE R.hotel_name = H.hotel_name
                AND R.price >= {minPrice} 
                AND R.price <= {maxPrice}
                ORDER BY hotel_name ASC;
            """)
        context = {
            "data" : data,
        }
    else:
        context = {
            "none" : "data",
        }
    return render(request, "daftar_hotel.html", context)

def detail_hotel(request, nib):
    data = query(f"""
                SELECT *
                FROM HOTEL
                WHERE nib = '{nib}';
            """)

    rooms = query(f"""
                    SELECT DISTINCT ON (R.number) 
                        R.number, R.price, RF.id
                    FROM 
                        HOTEL H
                    JOIN 
                        ROOM R ON H.hotel_name = R.hotel_name
                    JOIN 
                        ROOM_FACILITIES RF ON R.number = RF.rnum
                    WHERE 
                        H.nib = '{nib}'
                    ORDER BY 
                    R.number;
                """)
            
    if not data:
        return HttpResponse("Hotel not found", status=404)

    context = {
        'data': data[0],
        'rooms': rooms
    }
    return render(request, "detail_hotel.html", context)