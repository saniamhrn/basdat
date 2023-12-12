from django.shortcuts import render, redirect, HttpResponse
from utils.query import query
# Create your views here.

def checkRoleRedirect(request, expected):
    """
    -Hanya berfungsi untuk user sudah login
    -cek apakah session role sama seperti dengan expected, jika tidak redirect ke dashboard
    -contoh penggunaan:
    
    if not is_authenticated(request):
        return redirect('/login/?next=/trigger6/daftar_promo/')
    if checkRoleRedirect(request, 'admin') != 'admin':
        return redirect(checkRoleRedirect(request, 'admin'))
    """
    if get_session_data(request)['role']!= expected:
        role = get_session_data(request)['role']
        if role == 'admin':
            return "/dashboard/admin"
        if role == 'hotel':
            return "/dashboard/hotel"
        if role == 'customer':
            return "/dashboard/customer"
    return expected
        
def logreg(request):
    return render(request, "logreg.html")

def is_authenticated(request):
    try:
        request.session["email"]
        return True
    except KeyError:
        return False
    
def getrole(email):
    adminCheck = query(f"""
                       SELECT * FROM admin WHERE email='{email}'
                       """) 
    hotelCheck = query(f"""
                       SELECT * FROM hotel WHERE email='{email}'
                       """) 
    customerCheck = query(f"""
                          SELECT * FROM customer WHERE email='{email}'
                          """) 

    if adminCheck!=[]:
        return "admin"
    if hotelCheck!=[]:
        return "hotel"
    if customerCheck!=[]:
        return "customer"

def get_session_data(request):
    if not is_authenticated(request):
        return {}

    try:
        return {"email": request.session["email"], "role": request.session["role"]}
    except:
        return {}


def logout(request):
    next = request.GET.get("next")

    if not is_authenticated(request):
        return redirect("/")

    request.session.flush()
    request.session.clear_expired()

    if next != None and next != "None":
        return redirect(next)
    else:
        return redirect("/")
    
def login(request):
    next = request.GET.get("next")
    if is_authenticated(request):
        role = getrole(request.session["email"])
        if role == "admin":
            return redirect("/dashboard/admin")
        if role == "hotel":
            return redirect("/dashboard/hotel")
        if role == "customer":
            return redirect("/dashboard/customer")
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        userCheck = query(f"""
                          SELECT * FROM user_table WHERE email='{email}' and password = '{password}'
                          """) 
        # print(query(f"""SELECT email,password FROM USER_ACC WHERE email='{email}'""") )
        flag = is_authenticated(request)
        if userCheck!=[] and not flag:
            request.session["email"] = email
            request.session["password"] = password
            request.session["role"] = getrole(email)
            request.session.set_expiry(500)
            request.session.modified = True
            if next != None and next != "None":
                return redirect(next)
            else:
                role = getrole(email)
                if role == "admin":
                    return redirect("/dashboard/admin")
                if role == "hotel":
                    return redirect("/dashboard/hotel")
                if role == "pelanggan":
                    return redirect("/dashboard/customer")

    return render(request, "login.html")

def logout(request):
    return render(request, "logout.html")

def register(request):
    return render(request, "register.html")

def register_admin(request):
    # TODO: implement trigger auth
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nama = request.POST.get('nama')
        nomerhp = request.POST.get('nomerhp')
        
        # cek tidak ada nama belakang
        # if " " in nama:
        #     nama = request.POST.get('nama').split(" ",1)
        #     fname = nama[0]
        #     lname = nama[1]
        # else:
            # context = {'message': "Nama harus memiliki nama belakang"}
            # return render(request, "register_admin.html", context)
        
        emailCheck = query(f"""
                           SELECT * FROM USER_TABLE WHERE email='{email}'
                           """) 
        if emailCheck==[] and nama is not None:
            query(f"""
                  INSERT INTO USER_TABLE VALUES ('{email}', '{password}', '{nama}', '{0}')
                  """)
            query(f"""
                  INSERT INTO ADMIN VALUES ('{email}')
                  """)
            return redirect('login_logout:login')
        
        context = {'message': "Email sudah pernah terdaftar"}
        return render(request, "register_admin.html", context)
    context = {'message': ""}
    
    return render(request, "register_admin.html", context)


def register_customer(request):
    # TODO: implement trigger auth
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        nomerhp = request.POST.get('nomerhp')
        nik = request.POST.get('nik')
        
        # cek email belum terdaftar
        emailCheck = query(f"""
                           SELECT * FROM USER_TABLE WHERE email='{email}'
                           """) 
        if emailCheck==[]:
            query(f"""
                  INSERT INTO CUSTOMER VALUES ('{email}', '{nik}')
                  """)
            query(f"""
                  INSERT INTO USER_TABLE VALUES ('{email}', '{password}', '{fname}', '{lname}')
                  """)
            query(f"""
                  INSERT INTO RESERVATION_ACTOR VALUES ('{email}', '{nomerhp}', '{0}')
                  """)
            return redirect('login_logout:login')
        
        context = {'message': "Email sudah pernah terdaftar"}
        return render(request, "register_customer.html", context)
    
    context = {'message': ""}
    return render(request, "register_customer.html", context)

def register_hotel(request):
    # TODO: implement trigger auth    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nama = request.POST.get('nama')
        nomerhp = request.POST.get('nomerhp')
        
        # attr subclass
        hotel_name = request.POST.get('hotel_name')
        hotel_branch = request.POST.get('hotel_branch')
        nib = request.POST.get('nib')
        rating = request.POST.get('rating')
        star = request.POST.get('star')
        street = request.POST.get('street')
        district = request.POST.get('district')
        city = request.POST.get('city')
        province = request.POST.get('province')
        description = request.POST.get('description') 
        
        # cek tidak ada nama belakang
        if " " in nama:
            nama = request.POST.get('nama').split(" ",1)
            fname = nama[0]
            lname = nama[1]
        else:
            context = {
                'message': "Nama harus memiliki nama belakang",
            }
            context = {'message': "Nama harus memiliki nama belakang"}
            return render(request, "register_hotel.html",context) 

        # cek email belum terdaftar
        emailCheck = query(f"""
                           SELECT * FROM USER_TABLE WHERE email='{email}'
                           """) 
        if emailCheck==[]:
            query(f"""
                  INSERT INTO USER_TABLE VALUES ('{email}', '{password}', '{fname}', '{lname}')
                  """)
            query(f"""
                  INSERT INTO RESERVATION_ACTOR VALUES ('{email}', '{nomerhp}', '{0}')
                  """)
            query(f"""
                  INSERT INTO HOTEL VALUES ('{email}', '{hotel_name}', '{hotel_branch}', '{nib}', '{0}', '{0}', '{street}', '{district}', '{city}', '{province}', '{description}')
                  """)
            return redirect('login_logout:login')
        
        context = {
            'message': "Email sudah pernah terdaftar",
            }
        return render(request, "register_hotel.html",context)
    
    context = {
        'message': "",
        }
    return render(request, "register_hotel.html", context)