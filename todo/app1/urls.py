from django.urls import path
from .views import *
urlpatterns = [
    path('home/', Asosiy.as_view(), name="home"),
    path('', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('reja/<int:son>/', Reja_ochir.as_view()),
]