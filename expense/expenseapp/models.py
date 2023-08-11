from django.db import models

# Create your models here.
#Django ORM - Object Relational Mapper
#create table product(id,name varchar(200),price float,qty int,description varchar(500))

class Product(models.Model):
    name=models.CharField(max_length=200)
    price=models.FloatField()
    qty=models.IntegerField()
    description=models.TextField()
    color=models.CharField(max_length=15)
    saleunit=models.IntegerField(null=True)


    #to show object name
    def __str__(self):
        return self.name


    #by default it create table name like expenseapp_product in your database
    #so we can use MetaData to assign table name
    class Meta:
        db_table="product"


#foreign Key

class Author(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    age=models.IntegerField()

    def __str__(self):
        return self.name
    
    class Meta:
        db_table="author"


class Publication(models.Model):
    pname=models.CharField(max_length=200)
    year=models.IntegerField()
    place=models.CharField(max_length=200)

    def __str__(self):
        return self.pname
    
    class Meta:
        db_table="publication"



genere=(("science","science"),("fiction","fiction"),("drama","drama"),("action","action"))
class Books(models.Model):
    bname=models.CharField(max_length=200)
    bprice=models.FloatField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)            #this is nothing but author_id
    book_genere=models.CharField(max_length=200,choices=genere)
    publication=models.ForeignKey(Publication,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.bname
    
    class Meta:
        db_table="books"