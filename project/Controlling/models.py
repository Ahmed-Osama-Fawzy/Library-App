from django.db import models
from django.utils.timezone import now

class Book(models.Model):
    Id = models.PositiveIntegerField(primary_key=True)
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Category = models.CharField(max_length=50,null=True)
    Description = models.TextField()
    Available = models.BooleanField(default=False)
    Cover = models.ImageField(upload_to='static/Covers-%y-%m-%d')
    BorrowingNumber = models.IntegerField(default=0)
    def __str__(self):
        return str(self.Id)
    

class Admin(models.Model):
    Id = models.PositiveIntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    UserName = models.CharField(max_length=30,unique=True)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=13)
    def __str__(self):
        return str(self.Id)


class Client(models.Model):
    Id = models.PositiveIntegerField(primary_key=True)
    Name = models.CharField(max_length=30)
    UserName = models.CharField(max_length=30,unique=True)
    Email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=13)
    def __str__(self):
        return str(self.Id)


class Borrowing(models.Model):
    Id = models.PositiveIntegerField(primary_key=True)
    BorrowDate = models.DateField(default=now)
    ReturnDate = models.DateField(default=now)
    BookId = models.ForeignKey(Book,on_delete=models.CASCADE,default=1)
    def __str__(self):
        return str(self.Id)
    

class User(models.Model):
    Id = models.PositiveIntegerField(unique=True,auto_created=False)
    Rule = models.BooleanField(default=True)
    Password = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return str(self.Rule)