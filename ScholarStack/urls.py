from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('notFound', views.error_404, name='notFound'),
    path('error', views.error_500, name='error'),
    path('auth/signin', views.sign_in, name='login'),
    path('auth/signup', views.register, name='register'),
    path('home', views.home, name='home'),
    path('explore', views.explore, name='explore'),
    path('thesis/upload', views.create_thesis, name='upload-thesis'),
    path('thesis/watch/<int:id>', views.show_thesis, name='watch-thesis'),
    path('thesis/update/<int:id>', views.edit_thesis, name='edith-thesis'),
    path('auth/signout', views.sign_out, name='logout'),
    path('', views.index, name='index'),
]
