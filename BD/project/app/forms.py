from django import forms
from .models import VideoLibrary, Staff, Rank, Payment, Attendance, Income, Genre, Films, Equipment, FilmReview


class VideoLibraryForm(forms.ModelForm):

    # def __str__(self):
    #     # return f"{self.shop_name},{self.adress }"
    #     return f'{self.shop_name}, {self.id}'
    #     # return self.shop_name + ' ' + self.adress

    class Meta:

        model = VideoLibrary

        fields = [
            'shop_name',
            'adress',
        ]


class StaffForm(forms.ModelForm):

    # def __str__(self):
    #     return f'{self.staff_name}, {self.gender}'

    class Meta:

        model = Staff

        fields = [
            'staff_name',
            'living_adress',
            'gender',
            'age',
            'staff_rating',
            'shop_name',
        ]


class RankForm(forms.ModelForm):

    class Meta:

        model = Rank

        fields = [
            'staff_name',
            'rank_name',
        ]


class PaymentForm(forms.ModelForm):

    class Meta:

        model = Payment

        fields = [
            'rank_name',
            'payment_amount',
        ]


class AttendanceForm(forms.ModelForm):

    class Meta:

        model = Attendance

        fields = [
            'shop_name',
            'attendance_amount',
        ]


class IncomeForm(forms.ModelForm):

    class Meta:

        model = Income

        fields = [
            'shop_name',
            'income_amount',
        ]


class GenreForm(forms.ModelForm):

    class Meta:

        model = Genre

        fields = [
            'shop_name',
            'genre_name',
        ]


class FilmsForm(forms.ModelForm):

    class Meta:

        model = Films

        fields = [
            'shop_name',
            'genre_name',
            'film_name',
            'copies_amount',
            'film_cost',
        ]


class EquipmentForm(forms.ModelForm):

    class Meta:

        model = Equipment

        fields = [
            'shop_name',
            'equipment_name',
        ]


class FilmReviewForm(forms.ModelForm):

    class Meta:

        model = FilmReview

        fields = [
            'film_name',
            'review_amount',
            'review_score',
        ]
