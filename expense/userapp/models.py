from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    is_user=models.BooleanField(default=False)
    # is_developer=models.BooleanField(default=False)
    contact=models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.username
    
    class Meta:
        db_table='user'


class ExpenseDetail(models.Model):
    desc=models.CharField(max_length=200)
    amount=models.FloatField()
    category=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.desc
    
    class Meta:
        db_table='expensedetail'
