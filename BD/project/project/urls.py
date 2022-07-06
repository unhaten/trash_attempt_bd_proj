"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('main/', views.main, name='main'),
    path('create_shop/', views.create_shop, name='create_shop'),
    path('list_view/', views.list_view, name='list_view'),
    path('shop/<id>/', views.detail_shop, name='detail_shop'),
    path('staff/<id>/', views.detail_staff, name='detail_staff'),
    path('rank/<id>/', views.detail_rank, name='detail_rank'),
    path('payment/<id>/', views.detail_payment, name='detail_payment'),
    path('attendance/<id>/', views.detail_attendance, name='detail_attendance'),
    path('income/<id>/', views.detail_income, name='detail_income'),
    path('genre/<id>/', views.detail_genre, name='detail_genre'),
    path('film/<id>/', views.detail_film, name='detail_film'),
    path('equipment/<id>/', views.detail_equipment, name='detail_equipment'),
    path('film_review/<id>/', views.detail_film_review, name='detail_film_review'),
    path('shop/<id>/update', views.update_shop, name='update_shop'),
    path('staff/<id>/update', views.update_staff, name='update_staff'),
    path('rank/<id>/update', views.update_rank, name='update_rank'),
    path('payment/<id>/update', views.update_payment, name='update_payment'),
    path('attendance/<id>/update', views.update_attendance,
         name='update_attendance'),
    path('income/<id>/update', views.update_income, name='update_income'),
    path('genre/<id>/update', views.update_genre, name='update_genre'),
    path('film/<id>/update', views.update_film, name='update_film'),
    path('equipment/<id>/update', views.update_equipment, name='update_equipment'),
    path('film_review/<id>/update', views.update_film_review,
         name='update_film_review'),
    path('<id>/delete', views.delete_view, name='delete_view'),
    path('shop/<id>/delete', views.delete_shop, name='delete_shop'),
    path('staff/<id>/delete', views.delete_staff, name='delete_staff'),
    path('rank/<id>/delete', views.delete_rank, name='delete_rank'),
    path('payment/<id>/delete', views.delete_payment, name='delete_payment'),
    path('attendance/<id>/delete', views.delete_attendance,
         name='delete_attendance'),
    path('income/<id>/delete', views.delete_income, name='delete_income'),
    path('genre/<id>/delete', views.delete_genre, name='delete_genre'),
    path('film/<id>/delete', views.delete_film, name='delete_film'),
    path('equipment/<id>/delete', views.delete_equipment, name='delete_equipment'),
    path('film_review/<id>/delete', views.delete_film_review,
         name='delete_film_review'),
    path('create_staff/', views.create_staff, name='create_staff'),
    path('create_rank/', views.create_rank, name='create_rank'),
    path('create_payment/', views.create_payment, name='create_payment'),
    path('create_attendance/', views.create_attendance, name='create_attendance'),
    path('create_income/', views.create_income, name='create_income'),
    path('create_genre/', views.create_genre, name='create_genre'),
    path('create_film/', views.create_film, name='create_film'),
    path('create_equipment/', views.create_equipment, name='create_equipment'),
    path('create_film_review/', views.create_film_review,
         name='create_film_review'),
    path('create_view/', views.create_view, name='create_view'),

]
