
# Hotel Management Systems

Welcome to the Hotel Management System project! This repository contains the source code and documentation for a web-based hotel management system built using Django and PostgreSQL.



## Overview

The Hotel Management System is designed to manage the operations of a hotel, including room bookings, customer management, hotel & room facility management, and shuttle reservation. The system is built using Django for the backend and PostgreSQL for the database.
## 🧐 Features

- User authentication (staff and customers)
- Room booking and availability management
- Hotel & room facilities management
- Customer information management
- Payment tracking
- Shuttle reservation



## Installation

### Prerequisites
- Python 3.x
- PostgreSQL
- Git


### Steps
```bash
git clone https://github.com/saniamhrn/basdat.git
cd basdat
```

### Create and activate a virtual environment:
```bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`
```

### Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Set up the PostgreSQL database:
- Create a new PostgreSQL database.
- Update the DATABASES setting in settings.py with your database credentials.

### Run database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a superuser:
```bash
python manage.py createsuperuser
```

### Run the development server:
```bash
python manage.py runserver
```
    
## Usage/Examples

- Access the application at http://localhost:8000.
- Log in with the superuser account you created.
- Navigate through the application to manage rooms, bookings, customers, and shuttle.


## Project Structure
```bash
basdat/
├── basdut/                      # Django project directory
│   ├── settings.py              # Django settings file
│   ├── urls.py                  # URL configuration
│   ├── wsgi.py                  # WSGI configuration
│   └── ...
├── daftar_hotel/                # App for managing bookings (customers)
│   ├── migrations/              # Database migrations
│   ├── models.py                # Database models
│   ├── views.py                 # View functions
│   └── ...
├── daftar_reservasi/            # App for reservation (customers)
│   └── ...
├── dashboard/                   # App for dashboard
│   └── ...
├── fasilitas_hotel/             # App for hotel facility management
│   └── ...
├── kamar_hotel/                 # App for room management
│   └── ...
├── login_logout/                # App for user authentication
│   └── ...
├── menambah_review/             # App for adding review (customers)
│   └── ...
├── reservasi/                   # App for reservation management
│   └── ...
├── shuttle_reserve/             # App for shuttle reservation management
│   └── ...
├── templates/                   # HTML templates
│   └── ...
├── static/                      # Static files (CSS, JS, images)
│   └── ...
├── utils/                       # Query for SQL
│   └── ...
├── manage.py                    # Django management script
└── requirements.txt             # Python dependencies
```
