from django.contrib.auth.models import User

# Создайте пользователя и сохраните его в базе данных
user = User.objects.create_user('myusername', 'myemail@crazymail.com', 'mypassword')

