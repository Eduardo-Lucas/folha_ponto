from django.urls import path
from .views import NewLoginView, logout_view

app_name = "users"

urlpatterns = [
    path("login/", NewLoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
]
