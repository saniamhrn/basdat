from django.shortcuts import render, HttpResponse, redirect
from utils.query import query

def menambah_review(request, hotel_name):
    if request.method == 'POST':
        cust_email = request.POST.get('cust_email')
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        hotel_branch = request.POST.get('hotel_branch')

        query(f"""
            INSERT INTO reviews (id, cust_email, rating, review, hotel_name, hotel_branch) 
            VALUES ((SELECT MAX(id::INTEGER)+1 FROM reviews), '{cust_email}', '{rating}', '{review}', '{hotel_name}', '{hotel_branch}');
        """)

        query(f"""
            WITH RatingStats AS (
                SELECT
                    ROUND(AVG(R.rating), 1) AS average_rating,
                    SUM(R.rating) AS sum_data
                FROM
                    reviews R
                WHERE
                    R.hotel_name = 'Saros'
            )
            UPDATE hotel H
            SET
                star = (SELECT average_rating FROM RatingStats),
                rating = (SELECT sum_data FROM RatingStats)
            WHERE
                H.hotel_name = 'Saros';
        """)
        return redirect('dashboard:show_customer')
    else:
        hotel = query(f"""
                SELECT hotel_name, hotel_branch
                FROM HOTEL
                WHERE hotel_name = '{hotel_name}';
            """)

        if not hotel:
            return HttpResponse("Hotel not found", status=404)
        
        return render(request, 'menambah_review.html', {'hotel': hotel[0]})
