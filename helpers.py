import random
import string
import requests


BASE_URL = "https://qa-stellarburgers.education-services.ru/api"


def generate_random_string(length):
    """Генерирует случайную строку из букв нижнего регистра"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def register_new_user_and_return_login_password():
    """Регистрирует нового пользователя и возвращает [email, password, name]"""
    login_pass = []
    email = f"{generate_random_string(10)}@yandex.ru"
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(f"{BASE_URL}/auth/register", json=payload)

    if response.status_code == 200:
        login_pass.append(email)
        login_pass.append(password)
        login_pass.append(name)

    return login_pass

def create_order_with_auth(token, ingredient_ids):
    """Создает заказ через API с авторизацией"""
    headers = {"Authorization": token}
    payload = {"ingredients": ingredient_ids}
    response = requests.post(f"{BASE_URL}/orders", json=payload, headers=headers)
    return response