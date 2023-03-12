DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOSTNAME": "localhost",
        "NAME": "budget-nuggets",
        "USER": "budget-nuggets-user",
        "PASSWORD": "budget-nuggets-user",
        "OPTIONS": {},
    }
}

CORS_ALLOWED_ORIGINS = ["http://localhost:5173", "http://127.0.0.1:5173"]
