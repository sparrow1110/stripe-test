import os
from django.contrib.auth import get_user_model

from dotenv import load_dotenv
load_dotenv()

# Настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stripe_test.settings')
import django
django.setup()

User = get_user_model()

USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
EMAIL = os.getenv('ADMIN_EMAIL', 'admin@example.com')
PASSWORD = os.getenv('ADMIN_PASSWORD', 'root')

if not User.objects.filter(username=USERNAME).exists():
    print(f"Создаём суперюзера: {USERNAME} / {PASSWORD}")
    User.objects.create_superuser(
        username=USERNAME,
        email=EMAIL,
        password=PASSWORD
    )
    print("Суперюзер успешно создан!")
else:
    print("Суперюзер уже существует — пропускаем")