from django.db import models # Аналог таблицы books в sql
from django.contrib.auth.models import AbstractUser
#связуемая единица между sql и django
class User(AbstractUser):
    ROLE_CHOICES = [
        ('user', 'Обычный пользователь'),
        ('admin', 'Администратор'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')#Создание поле, которое хранит роль пользователя

    class Meta:
        db_table = 'echo_user'  # название таблички


class Book(models.Model):
    id = models.BigAutoField(primary_key=True) #автоинкрементное поле!!!
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=100, null=True, blank=True)
    publication_year = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'books'  # Указываем имя таблицы, если оно отличается от имени модели

    def __str__(self):
        return self.title

# выполняем команду миграций->
# джанго выполняет в постгрисе sql запрос, который выше
# через методы all, save(эквиваленты select*, insert into) мы можем рботать с базой данных
# через этот код