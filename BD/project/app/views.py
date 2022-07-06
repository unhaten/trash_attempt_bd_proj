from multiprocessing import context
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from app.models import VideoLibrary, Staff, Rank, Payment, Attendance, Income, Genre, Films, Equipment, FilmReview
from app.forms import VideoLibraryForm, StaffForm, RankForm, PaymentForm, AttendanceForm, IncomeForm, GenreForm, FilmsForm, EquipmentForm, FilmReviewForm

# Create your views here.


def index(request):

    return render(request, 'app/index.html')


def main(request):

    library_list = VideoLibrary.objects.order_by('shop_name')
    adress_list = VideoLibrary.objects.order_by('adress')
    library_dict = {'shop_name': library_list, 'adress': adress_list}

    return render(request, 'app/main.html', context=library_dict)

# *******************************************************************************************************************************************

# TODO: CREATE PAGES


def create_shop(request):
    # dict for initial data with field names as keys
    context = {}

    # add dict during the initialization
    library_form = VideoLibraryForm(request.POST or None)
    if library_form.is_valid():
        library_form.save()

    context['library_form'] = library_form

    return render(request, 'create/create_shop.html', context)


def create_staff(request):
    context = {}

    staff_form = StaffForm(request.POST or None)
    if staff_form.is_valid():
        staff_form.save()

    context['staff_form'] = staff_form

    return render(request, 'create/create_staff.html', context)


def create_rank(request):
    context = {}

    rank_form = RankForm(request.POST or None)
    if rank_form.is_valid():
        rank_form.save()

    context['rank_form'] = rank_form

    return render(request, 'create/create_rank.html', context)


def create_payment(request):
    context = {}

    payment_form = PaymentForm(request.POST or None)
    if payment_form.is_valid():
        payment_form.save()

    context['payment_form'] = payment_form

    return render(request, 'create/create_payment.html', context)


def create_attendance(request):
    context = {}

    attendance_form = AttendanceForm(request.POST or None)
    if attendance_form.is_valid():
        attendance_form.save()

    context['attendance_form'] = attendance_form

    return render(request, 'create/create_attendance.html', context)


def create_income(request):
    context = {}

    income_form = IncomeForm(request.POST or None)
    if income_form.is_valid():
        income_form.save()

    context['income_form'] = income_form

    return render(request, 'create/create_income.html', context)


def create_genre(request):
    context = {}

    genre_form = GenreForm(request.POST or None)
    if genre_form.is_valid():
        genre_form.save()

    context['genre_form'] = genre_form

    return render(request, 'create/create_genre.html', context)


def create_film(request):
    context = {}

    films_form = FilmsForm(request.POST or None)
    if films_form.is_valid():
        films_form.save()

    context['films_form'] = films_form

    return render(request, 'create/create_film.html', context)


def create_equipment(request):
    context = {}

    equipment_form = EquipmentForm(request.POST or None)
    if equipment_form.is_valid():
        equipment_form.save()

    context['equipment_form'] = equipment_form

    return render(request, 'create/create_equipment.html', context)


def create_film_review(request):
    context = {}

    film_review_form = FilmReviewForm(request.POST or None)
    if film_review_form.is_valid():
        film_review_form.save()

    context['film_review_form'] = film_review_form

    return render(request, 'create/create_film_review.html', context)

# TODO: END OF CREATE PAGES

# *******************************************************************************************************************************************


def list_view(request):

    context = {}

    context['library_dataset'] = VideoLibrary.objects.all()
    context['staff_dataset'] = Staff.objects.all()
    context['rank_dataset'] = Rank.objects.all()
    context['payment_dataset'] = Payment.objects.all()
    context['attendance_dataset'] = Attendance.objects.all()
    context['income_dataset'] = Income.objects.all()
    context['genre_dataset'] = Genre.objects.all()
    context['films_dataset'] = Films.objects.all()
    context['equipment_dataset'] = Equipment.objects.all()
    context['film_review_dataset'] = FilmReview.objects.all()

    # context['dataset'] = VideoLibrary.objects.all().filter(shop_name__icontains = 'Gamers')

    return render(request, 'app/list_view.html', context)


# *******************************************************************************************************************************************


# TODO: UPDATE PAGES

def update_shop(request, id):
    context = {}

# * fetch the object related to passed id
    obj_shop = get_object_or_404(VideoLibrary, id=id)


# * pass the object as instance in form
    form_shop = VideoLibraryForm(request.POST or None, instance=obj_shop)


# * save the data from the form and
# * redirect to detail_view

    if form_shop.is_valid():
        form_shop.save()
        return HttpResponseRedirect('/main/')

    context['form_shop'] = form_shop

    return render(request, 'update/update_shop.html', context)


def update_staff(request, id):
    context = {}

    obj_staff = get_object_or_404(Staff, id=id)
    form_staff = StaffForm(request.POST or None, instance=obj_staff)

    if form_staff.is_valid():
        form_staff.save()
        return HttpResponseRedirect('/main/')

    context['form_staff'] = form_staff

    return render(request, 'update/update_staff.html', context)


def update_rank(request, id):
    context = {}

    obj_rank = get_object_or_404(Rank, id=id)

    form_rank = RankForm(request.POST or None, instance=obj_rank)

    if form_rank.is_valid():
        form_rank.save()
        return HttpResponseRedirect('/main/')

    context['form_rank'] = form_rank

    return render(request, 'update/update_rank.html', context)


def update_payment(request, id):
    context = {}

    obj_payment = get_object_or_404(Payment, id=id)

    form_payment = PaymentForm(request.POST or None, instance=obj_payment)

    if form_payment.is_valid():
        form_payment.save()
        return HttpResponseRedirect('/main/')

    context['form_payment'] = form_payment

    return render(request, 'update/update_payment.html', context)


def update_attendance(request, id):
    context = {}

    obj_attendance = get_object_or_404(Attendance, id=id)

    form_attendance = AttendanceForm(
        request.POST or None, instance=obj_attendance)

    if form_attendance.is_valid():
        form_attendance.save()
        return HttpResponseRedirect('/main/')

    context['form_attendance'] = form_attendance

    return render(request, 'update/update_attendance.html', context)


def update_income(request, id):
    context = {}

    obj_income = get_object_or_404(Income, id=id)

    form_income = IncomeForm(request.POST or None, instance=obj_income)

    if form_income.is_valid():
        form_income.save()
        return HttpResponseRedirect('/main/')

    context['form_income'] = form_income

    return render(request, 'update/update_income.html', context)


def update_genre(request, id):
    context = {}

    obj_genre = get_object_or_404(Genre, id=id)

    form_genre = GenreForm(request.POST or None, instance=obj_genre)

    if form_genre.is_valid():
        form_genre.save()
        return HttpResponseRedirect('/main/')

    context['form_genre'] = form_genre

    return render(request, 'update/update_genre.html', context)


def update_film(request, id):
    context = {}

    obj_film = get_object_or_404(Films, id=id)

    form_film = FilmsForm(request.POST or None, instance=obj_film)

    if form_film.is_valid():
        form_film.save()
        return HttpResponseRedirect('/main/')

    context['form_film'] = form_film

    return render(request, 'update/update_film.html', context)


def update_equipment(request, id):
    context = {}

    obj_equipment = get_object_or_404(Equipment, id=id)

    form_equipment = EquipmentForm(
        request.POST or None, instance=obj_equipment)

    if form_equipment.is_valid():
        form_equipment.save()
        return HttpResponseRedirect('/main/')

    context['form_equipment'] = form_equipment

    return render(request, 'update/update_equipment.html', context)


def update_film_review(request, id):
    context = {}

    obj_film_review = get_object_or_404(FilmReview, id=id)

    form_film_review = FilmReviewForm(
        request.POST or None, instance=obj_film_review)

    if form_film_review.is_valid():
        form_film_review.save()
        return HttpResponseRedirect('/main/')

    context['form_film_review'] = form_film_review

    return render(request, 'update/update_film_review.html', context)


# TODO: END OF UPDATE PAGES

# *******************************************************************************************************************************************

# TODO: DETAILED PAGES

def detail_shop(request, id):
    context = {}

    context['shop'] = VideoLibrary.objects.get(id=id)

    return render(request, 'detail/detail_shop.html', context)


def detail_staff(request, id):
    context = {}

    # context['shop'] = VideoLibrary.objects.get(id=id)
    context['staff'] = Staff.objects.get(id=id)

    return render(request, 'detail/detail_staff.html', context)


def detail_rank(request, id):
    context = {}

    # context['staff'] = Staff.objects.get(id=id)
    context['rank'] = Rank.objects.get(id=id)

    return render(request, 'detail/detail_rank.html', context)


def detail_payment(request, id):
    context = {}

    # context['staff'] = Staff.objects.get(id=id)
    # context['rank'] = Rank.objects.get(id=id)
    context['payment'] = Payment.objects.get(id=id)

    return render(request, 'detail/detail_payment.html', context)


def detail_attendance(request, id):
    context = {}

    # context['shop'] = VideoLibrary.objects.get(id=id)
    context['attendance'] = Attendance.objects.get(id=id)

    return render(request, 'detail/detail_attendance.html', context)


def detail_income(request, id):
    context = {}

    # context['shop'] = VideoLibrary.objects.get(id=id)
    context['income'] = Income.objects.get(id=id)

    return render(request, 'detail/detail_income.html', context)


def detail_genre(request, id):
    context = {}

    # context['shop'] = VideoLibrary.objects.get(id=id)
    context['genre'] = Genre.objects.get(id=id)

    return render(request, 'detail/detail_genre.html', context)


def detail_film(request, id):
    context = {}

    # context['shop'] = VideoLibrary.objects.get(id=id)
    # context['genre'] = Genre.objects.get(id=id)
    context['film'] = Films.objects.get(id=id)

    return render(request, 'detail/detail_film.html', context)


def detail_equipment(request, id):
    context = {}

    # context['shop'] = VideoLibrary.objects.get(id=id)    
    context['equipment'] = Equipment.objects.get(id=id)

    return render(request, 'detail/detail_equipment.html', context)


def detail_film_review(request, id):
    context = {}

    # context['film'] = Films.objects.get(id=id)
    context['film_review'] = FilmReview.objects.get(id=id)

    return render(request, 'detail/detail_film_review.html', context)

# TODO: END OF DETAILED PAGES

# *******************************************************************************************************************************************

# TODO: DELETING OF OBJECTS

def delete_view(request, id):

    context = {}

    obj = get_object_or_404(VideoLibrary, id=id)

    if request.method == 'POST':
        # delete object
        obj.delete()

        # after deleting redirect to
        # home page
        return HttpResponseRedirect('/')

    return render(request, 'app/delete_view.html', context)

def delete_shop(request, id):

    context = {}

    obj = get_object_or_404(VideoLibrary, id=id)

    if request.method == 'POST':
        obj.delete()

        return HttpResponseRedirect('/')

    return render(request, 'delete/delete_shop.html', context)

def delete_staff(request, id):

    context = {}

    obj = get_object_or_404(Staff, id=id)

    if request.method == 'POST':
        obj.delete()

        return HttpResponseRedirect('/')

    return render(request, 'delete/delete_staff.html', context)

def delete_rank(request, id):

    context = {}

    obj = get_object_or_404(Rank, id=id)

    if request.method == 'POST':
        # delete object
        obj.delete()

        # after deleting redirect to
        # home page
        return HttpResponseRedirect('/')

    return render(request, 'delete/delete_rank.html', context)

def delete_payment(request, id):

    context = {}

    obj = get_object_or_404(Payment, id=id)

    if request.method == 'POST':
        obj.delete()

        return HttpResponseRedirect('/')

    return render(request, 'delete/delete_payment.html', context)

def delete_attendance(request, id):

    context = {}

    obj = get_object_or_404(Attendance, id=id)

    if request.method == 'POST':
        obj.delete()

        return HttpResponseRedirect('/')

    return render(request, 'delete/delete_attendance.html', context)

def delete_income(request, id):

    context = {}

    obj = get_object_or_404(Income, id=id)

    if request.method == 'POST':
        obj.delete()

        return HttpResponseRedirect('/')

    return render(request, 'delete/delete_income.html', context)

def delete_genre(request, id):

    context = {}

    obj = get_object_or_404(Genre, id=id)

    if request.method == 'POST':
        obj.delete()

        return HttpResponseRedirect('/')

    return render(request, 'delete/delete_genre.html', context)

def delete_film(request, id):

    context = {}

    obj = get_object_or_404(Films, id=id)

    if request.method == 'POST':
        obj.delete()

        return HttpResponseRedirect('/')

    return render(request, 'delete/delete_film.html', context)

def delete_equipment(request, id):

    context = {}

    obj = get_object_or_404(Equipment, id=id)

    if request.method == 'POST':
        obj.delete()

        return HttpResponseRedirect('/')

    return render(request, 'delete/delete_equipment.html', context)

def delete_film_review(request, id):

    context = {}

    obj = get_object_or_404(FilmReview, id=id)

    if request.method == 'POST':
        obj.delete()

        return HttpResponseRedirect('/')

    return render(request, 'delete/delete_film_review.html', context)

# TODO: END OF DELETING OF OBJECTS

def create_view(request):

    context = {}

    return render(request, 'app/create_view.html', context)