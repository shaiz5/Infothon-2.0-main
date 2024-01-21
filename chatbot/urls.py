from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("", views.chatbot, name="chatbot"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
    path("change_lang", views.language_select, name="lang_change"),
    path("loc_services", views.loc_services, name="loc_services"),
]
