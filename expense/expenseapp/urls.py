from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
   path('home/',views.home),
   path('aboutus/',views.aboutus),
   path('contactus/',views.contactus),
   path('product/',views.getProduct),
   path('book/',views.getBook)

]
