import django


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

import random
from app.models import VideoLibrary, Staff, Rank, Payment, Attendance, Income, Genre, Films, Equipment, FilmReview
from faker import Faker
import faker_music

fakegen = Faker()
fakegen_m = Faker()

fakegen_m.add_provider(faker_music.MusicProvider)

def populate(N=5):

    for entry in range(N):
        
        shop_id = VideoLibrary.objects.order_by('?').first()
        staff_id = Staff.objects.order_by('?').first()
        rank_id = Rank.objects.order_by('?').first()
        genre_id = Genre.objects.order_by('?').first()
        film_id = Films.objects.order_by('?').first()
        fake_name = fakegen.name()
        fake_living_adress = fakegen.street_address()
        gender = random.choice(['Male', 'Female'])
        age = random.randint(1,100)
        staff_rating = random.randint(1,100)
        fake_shop = fakegen.company()
        fake_rank_name = fakegen.job()
        payment_amount = random.randint(100,10000)
        attendance_amount = random.randint(9,9999)
        fake_genre_name = fakegen_m.music_genre()
        fake_film_name = fakegen.cryptocurrency()
        fake_equipment_name = fakegen_m.music_instrument()

        shop = VideoLibrary.objects.get_or_create(shop_name = fake_shop, adress = fake_living_adress)
        staff = Staff.objects.get_or_create(shop_id = shop_id, nsf = fake_name, living_adress = fake_living_adress, gender = gender, age = age, staff_rating = staff_rating)[0]
        rank = Rank.objects.get_or_create(staff_id = staff_id, rank_name = fake_rank_name)
        payment = Payment.objects.get_or_create(rank_id = rank_id, payment_amount = payment_amount)
        attendance = Attendance.objects.get_or_create(shop_id=shop_id, attendance_amount = attendance_amount)
        income = Income.objects.get_or_create(shop_id = shop_id, income_amount = payment_amount)
        genre = Genre.objects.get_or_create(shop_id = shop_id, genre_name = fake_genre_name)
        films = Films.objects.get_or_create(shop_id = shop_id, genre_id = genre_id, film_name = fake_film_name, copies_amount = attendance_amount, film_cost = age)
        equipment = Equipment.objects.get_or_create(shop_id = shop_id, equipment_name = fake_equipment_name)
        film_review = FilmReview.objects.get_or_create(film_id = film_id, review_amount = attendance_amount, review_score = staff_rating)

if __name__ == '__main__':
    print('populating script!')
    populate(5)
    print('populating complete!')
