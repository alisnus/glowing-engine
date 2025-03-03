from django.urls import path
from . import views
from .views import check_email

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add/', views.addBook, name='add_book'),
    path('edit/<int:pk>/', views.editBook, name='edit_book'),
    path('delete/<int:pk>/', views.deleteBook, name='delete_book'),
    path('check-email/', views.check_email, name='check_email'),
]
