from django.urls import path
from .views import *


app_name = "users"

urlpatterns = [
    path("register/", Register.as_view(), name="register"),
]