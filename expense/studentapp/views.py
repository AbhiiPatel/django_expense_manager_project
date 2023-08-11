from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from .models import Student
# Create your views here.
#Two types of Views-Function based views and Class based views

class RegisterStudent(CreateView):
    template_name="student/register.html"
    model=Student
    success_url="/studentapp/list"
    # fields=["name","email","password","age"]
    fields="__all__"


class ListStudent(ListView):
    context_object_name="students"
    model=Student
    template_name="student/list.html"


class DeleteStudent(DeleteView):
    model=Student
    template_name="student/delete.html"
    success_url="/studentapp/list"


class UpdateStudent(UpdateView):
    template_name="student/update.html"
    model=Student
    success_url="/studentapp/list"
    fields="__all__"


class DetailStudent(DetailView):
    model=Student
    template_name="student/detail.html"
    context_object_name="students"


