from django.db import models

# Create your models here.


class VideoLibrary(models.Model):
    # shop_id = models.AutoField(primary_key=True, unique=True)
    shop_name = models.CharField(max_length=264)
    adress = models.TextField(max_length=264, default='')

    def __str__(self):
        # return f"{self.shop_name},{self.adress }"
        return f'{self.shop_name}, {self.id}'
        # return self.shop_name + ' ' + self.adress

    class Meta:
        verbose_name_plural = "Video Libraries"


class Staff(models.Model):
    # staff_id = models.AutoField(primary_key=True, unique=True)
    staff_name = models.CharField(max_length=264)
    living_adress = models.TextField(max_length=264)
    gender = models.CharField(max_length=264)
    age = models.IntegerField()
    staff_rating = models.IntegerField()
    shop_name = models.ForeignKey(VideoLibrary, on_delete=models.CASCADE)

    def __str__(self):
        # template = '{0.staff_name}, {0.gender}'
        return f'{self.staff_name}'
        # return template.render(self)

    class Meta:
        verbose_name_plural = "Staff"


class Rank(models.Model):
    # rank_id = models.AutoField(primary_key=True, unique=True)
    staff_name = models.ForeignKey(Staff, on_delete=models.CASCADE)
    rank_name = models.CharField(max_length=264)

    def __str__(self):
        return f'{self.rank_name}, {self.staff_name}'

    class Meta:
        verbose_name_plural = "Ranks"


class Payment(models.Model):
    # payment_id = models.AutoField(primary_key=True)
    rank_name = models.ForeignKey(Rank, on_delete=models.CASCADE)
    payment_amount = models.IntegerField()

    def __str__(self):
        return f'{self.rank_name}, {self.payment_amount}'

    class Meta:
        verbose_name_plural = "Payments"


class Attendance(models.Model):
    # attendance_id = models.AutoField(primary_key=True, unique=True)
    shop_name = models.ForeignKey(VideoLibrary, on_delete=models.CASCADE)
    attendance_amount = models.IntegerField()

    def __str__(self):
        return f'{self.shop_name}, {self.attendance_amount}'

    class Meta:
        verbose_name_plural = "Attendances"


class Income(models.Model):
    # income_id = models.AutoField(primary_key=True, unique=True)
    shop_name = models.ForeignKey(VideoLibrary, on_delete=models.CASCADE)
    income_amount = models.IntegerField()

    def __str__(self):
        return f'{self.shop_name}, {self.income_amount}, {self.id}'

    class Meta:
        verbose_name_plural = "Income"


class Genre(models.Model):
    # genre_id = models.AutoField(primary_key=True, unique=True)
    shop_name = models.ForeignKey(VideoLibrary, on_delete=models.CASCADE)
    genre_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name_plural = "Genres"


class Films(models.Model):
    # film_id = models.AutoField(primary_key=True, unique=True)
    shop_name = models.ForeignKey(VideoLibrary, on_delete=models.CASCADE)
    genre_name = models.ForeignKey(Genre, on_delete=models.CASCADE)
    film_name = models.CharField(max_length=264)
    copies_amount = models.IntegerField()
    film_cost = models.IntegerField()

    def __str__(self):
        return f'{self.film_name}, {self.genre_name}'

    class Meta:
        verbose_name_plural = "Films"


class Equipment(models.Model):
    # equipment_id = models.AutoField(primary_key=True, unique=True)
    shop_name = models.ForeignKey(VideoLibrary, on_delete=models.CASCADE)
    equipment_name = models.CharField(max_length=264)

    def __str__(self):
        return self.equipment_name

    class Meta:
        verbose_name_plural = "Equipment"


class FilmReview(models.Model):
    # film_review_id = models.AutoField(primary_key=True, unique=True)
    film_name = models.ForeignKey(Films, on_delete=models.CASCADE)
    review_amount = models.IntegerField()
    review_score = models.IntegerField()

    def __str__(self):
        return f'{self.film_name}, {self.review_score}'

    class Meta:
        verbose_name_plural = "Film Reviews"
