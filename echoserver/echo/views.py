from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import RegisterForm, BookForm #представления для отображения книг и функционал добавления, изменения и удаления
from django.core.paginator import Paginator
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.contrib.auth.models import User
#Обработчик запросов
User = get_user_model()

def check_email(request):
    email = request.GET.get("email")
    exists = User.objects.filter(email=email).exists()
    return JsonResponse({"exists": exists})

def is_admin(user):# Проверка роли пользователя
    return user.is_authenticated and user.role == 'admin'#свойство если пользователь зашёл

# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'echoserver/register.html', {'form': form})

# Вход пользователя
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'echoserver/login.html')

# Выход пользователя
def user_logout(request):
    logout(request)# Выход из системы
    return redirect('home')  # Перенаправляем на страницу входа после выхода

def homePageView(request):
    books = Book.objects.all()#таскаем данные из постгриса

    paginator = Paginator(books, 5)  # 5 книг на страницу
    page_number = request.GET.get('page')  # Получаем номер текущей страницы из запроса
    books = paginator.get_page(page_number)  # Загружаем книги для этой страницы
    return render(request, 'echoserver/home.html', {'books': books})
# Добавление книги
@login_required#когда неавторизованный пользователь пытается сюда попасть его кикает на страницу входа
def addBook(request):
    if request.method == 'POST':  #если челикс отправил форму то
        form = BookForm(request.POST) # создаём форму и заполняем её данными
        if form.is_valid(): #чекаем что данные коррректны
            form.save()#сохраняем новую книжонку в базу данных
            return redirect('home') #возвращаемся на главную страничку
    else:
        form = BookForm() #если челикс ещё ничего не отправлял, а только открыл форму
    return render(request, 'echoserver/add_book.html', {'form': form}) #передаём форму в шаблон!!!

# Редактирование книги (только для администратуса)
@login_required
@user_passes_test(is_admin)
def editBook(request, pk):
    book = get_object_or_404(Book, pk=pk) #ищем книгу по её id  дб
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request, 'echoserver/edit_book.html', {'form': form})

# Удаление книги (только для администратуса)
@login_required
@user_passes_test(is_admin)
def deleteBook(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'echoserver/delete_book.html', {'book': book})

def check_email(request):
    email = request.GET.get("email")
    exists = User.objects.filter(email=email).exists()
    return JsonResponse({"exists": exists})