from django.urls import path
from .views import *

urlpatterns = [
	
    path("", index),
    path("register/", register, name="register"),
    path("register_page/", register_page, name="register_page"),

    path("login_page/", login_page, name="login_page"),
    path("login/", login, name="login"),

    path("forgot_password/", forgot_password, name="forgot_password" ),
    #path("forgot_pwd/", forgot_pwd, name="forgot_pwd"),
]