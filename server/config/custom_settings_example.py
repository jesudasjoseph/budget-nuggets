DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "localhost",
        "PORT": "15432",
        "NAME": "budget_nuggets_db",
        "USER": "budget_nuggets_user",
        "PASSWORD": "dev_password",
        "OPTIONS": {},
    }
}

CORS_ALLOWED_ORIGINS = ["http://localhost:5173", "http://127.0.0.1:5173"]
