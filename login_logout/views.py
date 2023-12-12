from django.shortcuts import render, redirect, HttpResponse
from utils.query import query
# Create your views here.
def login(request):
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
        if " " in nama:
            nama = request.POST.get('nama').split(" ",1)
            fname = nama[0]
            lname = nama[1]
        else:
            # context = {'message': "Nama harus memiliki nama belakang"}
            return render(request, "register_admin.html",context)
        
        emailCheck = query(f"""
                           SELECT * FROM USER WHERE email='{email}'
                           """) 
        if emailCheck==[] and fname is not None:
            query(f"""
                  INSERT INTO USER VALUES ('{email}', '{password}', '{fname}', '{lname}')
                  """)
            query(f"""
                  INSERT INTO ADMIN VALUES ('{email}')
                  """)
            return redirect('login')
        
        context = {'message': "Email sudah pernah terdaftar"}
        return render(request, "register_admin.html",context)
    context = {'message': ""}
    
    return render(request, "register_admin.html", context)


def register_customer(request):
    # TODO: implement trigger auth
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        nama = request.POST.get('nama')
        nomerhp = request.POST.get('nomerhp')
        nik = request.POST.get('nik')
        # nama_bank = request.POST.get('nama_bank')
        # nomor_rekening = request.POST.get('nomor_rekening')
        
        # attr subclass
        # tanggal_lahir = request.POST.get('tanggal_lahir')
        # jenis_kelamin = "M" if request.POST.get('jenis_kelamin') == "Laki-Laki" else "F"
        
        # cek tidak ada nama belakang
        if " " in nama:
            nama = request.POST.get('nama').split(" ",1)
            fname = nama[0]
            lname = nama[1]
        else:
            context = {'message': "Nama harus memiliki nama belakang"}
            return render(request, "register_customer.html",context) 
        
        # cek email belum terdaftar
        emailCheck = query(f"""
                           SELECT * FROM USER WHERE email='{email}'
                           """) 
        if emailCheck==[]:
            query(f"""
                  INSERT INTO USER VALUES ('{email}', '{password}', '{fname}', '{lname}')
                  """)
            query(f"""
                  INSERT INTO RESERVATION_ACTOR VALUES ('{email}', '{nomerhp}', '{0}')
                  """)
            query(f"""
                  INSERT INTO CUSTOMER VALUES ('{email}', '{nik}')
                  """)
            return redirect('login')
        
        context = {'message': "Email sudah pernah terdaftar"}
        return render(request, "register_customer.html",context)
    
    context = {'message': ""}
    return render(request, "register_customer.html",context)

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
            return render(request, "register_restoran.html",context) 

        # cek email belum terdaftar
        emailCheck = query(f"""
                           SELECT * FROM USER WHERE email='{email}'
                           """) 
        if emailCheck==[]:
            query(f"""
                  INSERT INTO USER VALUES ('{email}', '{password}', '{fname}', '{lname}')
                  """)
            query(f"""
                  INSERT INTO RESERVATION_ACTOR VALUES ('{email}', '{nomerhp}', '{0}')
                  """)
            query(f"""
                  INSERT INTO HOTEL VALUES ('{email}', '{hotel_name}', '{hotel_branch}', '{nib}', '{0}', '{0}', '{street}', '{district}', '{city}', '{province}', '{description}')
                  """)
            return redirect('login')
        
        context = {
            'message': "Email sudah pernah terdaftar",
            }
        return render(request, "register_hotel.html",context)
    
    context = {
        'message': "",
        }
    return render(request, "register_hotel.html", context)