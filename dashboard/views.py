from django.shortcuts import render
from utils.query import query

# Create your views here.
def show_customer(request):
    data = query(f"""
                SELECT U.fname, U.lname, RA.email, RA.phonenum, C.nik
                FROM user_table U
                JOIN RESERVATION_ACTOR RA ON RA.email = U.email 
                LEFT JOIN CUSTOMER C ON C.email = RA.email;
                """)
    # print(data)

    context = {
        "data_cust" : data
    }
    return render(request, "dash_cust.html", context)

def show_hotel(request):
    data = query(f"""
                 SELECT 
                 h.street, h.district, h.city, h.province,
                 h.hotel_name, h.hotel_branch, h.nib, h.email,
                 ra.phonenum,
                 u.fname, u.lname
                 FROM hotel h
                 RIGHT JOIN reservation_actor ra ON h.email = ra.email
                 RIGHT JOIN user_table u ON h.email = u.email
                 WHERE ra.email LIKE '%.hotel%';
                 """)

    context= {
        "data_hotel" : data
    }
    return render(request, "dash_hotel.html", context)