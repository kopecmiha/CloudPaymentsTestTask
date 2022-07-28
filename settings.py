from os import environ

BASE_URL = 'https://api.cloudpayments.ru/'  # Корневой url api cloudpayments

PUBLIC_ID = environ.get("PUBLIC_ID", "some_id")  # Public ID из личного кабинета cloudpayments в качестве логина
API_SECRET = environ.get("API_SECRET", "some_secret")  # API_SECRET в качестве пароля
SERVICE = environ.get("SERVICE", "some_service")
