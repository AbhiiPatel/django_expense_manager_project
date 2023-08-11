from django.contrib import admin
from django.urls import path,include
from .views import UserRegisterView,UserLoginView,RegisterExpense,ListExpense,DeleteExpense,UpdateExpense
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    
    path('user_register/',UserRegisterView.as_view(),name="user_register"),
    path('login/',UserLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page="login"),name="logout"),
    path('register_expense/',RegisterExpense.as_view(),name="register_expense"),
    path('list_expense/',ListExpense.as_view(),name="list_expense"),
    path('delete_expense/<int:pk>',DeleteExpense.as_view(),name='delete_expense'),
    path('update_expense/<int:pk>',UpdateExpense.as_view(),name='update_expense'),
    # path('sendmail/',views.sendMail,name="sendmail")


]