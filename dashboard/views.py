from django.shortcuts import render
from utils.query import query

# Create your views here.
def show_customer(request):
    data = query(f"""
                SELECT U.fname, U.lname, RA.email, RA.phonenum, C.nik
	            FROM USER_TABLE U
	            JOIN RESERVATION_ACTOR RA ON U.email = RA.email
                LEFT JOIN CUSTOMER C ON RA.email = C.email;
                """)
    context = {
        "data" : data,
    }
    return render(request, "dash_cust.html", context)

def show_hotel(request):
    data = query(f"""SELECT
    A.Email AS Owner_Email,
    A.Fname AS Owner_FirstName,
    A.Lname AS Owner_LastName,
    RA.PhoneNum AS Hotel_PhoneNumber,
    H.Email AS Hotel_Email,
    H.NIB AS Hotel_NomorIzinUsaha,
    H.Hotel_Name AS Hotel_Name,
    H.Hotel_Branch AS Hotel_Branch,
    H.Street AS Hotel_Street,
    H.District AS Hotel_District,
    H.City AS Hotel_City,
    H.Province AS Hotel_Province
FROM
    ADMIN A
JOIN
    RESERVATION_ACTOR RA ON A.Email = RA.Admin_email
JOIN
    HOTEL H ON RA.Email = H.Email;
""")

    context= {
        "data" : data,
    }
    return render(request, "dash_hotel.html", context)