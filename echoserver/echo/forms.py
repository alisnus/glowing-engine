from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Book

class RegisterForm(UserCreationForm):# форму регистрации добавляем
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'role']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book #указываем с какой моделью работаем
        fields = ['title', 'author', 'price', 'genre', 'publication_year'] #определяем поля в форме
