from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import User,ExpenseDetail
from .forms import ExpenseUserCreationForm
from django.views.generic import CreateView,ListView,DeleteView,UpdateView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,'home.html')

def sendMail(to):
    
    subject = 'Welcome to Expesnse Manager'
    message = 'Hi , thank you for registering in expense manager project.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [to,]
    send_mail( subject, message, email_from, recipient_list )
    return True

class UserRegisterView(CreateView):
    model=User
    template_name="userapp/user_register.html"
    form_class=ExpenseUserCreationForm
    success_url="/"

    def form_valid(self, form):
        email=form.cleaned_data.get('email')
        print(email)
        sendMail(email)

        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name="userapp/login.html"
    success_url='/'
    
    def get_success_url(self):
        if self.request.user.is_authenticated:
            if self.request.user.is_superuser:
                return '/admin/'
            elif self.request.user.is_user:
                return '/user/register_expense/'
            
        else:
            return '/user/user_register/'
               
@method_decorator(login_required(login_url='login'),name='dispatch')
class RegisterExpense(CreateView):
    template_name='userapp/register_expense.html'
    model=ExpenseDetail
    success_url='/user/list_expense'
    fields=["desc","amount","category"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class ListExpense(ListView):
    model=ExpenseDetail
    template_name='userapp/list_expense.html'
    context_object_name='expenses'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        #select * from expense where user=self.request.user
        context['expenses']=ExpenseDetail.objects.filter(user=self.request.user)
        return context



class DeleteExpense(DeleteView):
    model=ExpenseDetail
    template_name='userapp/delete_expense.html'
    success_url='/user/list_expense'


class UpdateExpense(UpdateView):
    template_name='userapp/update_expense.html'
    model=ExpenseDetail
    success_url='/user/list_expense'
    fields='__all__'