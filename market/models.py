from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

mobile_regex = RegexValidator("^09(1[0-9]|3[1-9])-?[0-9]{3}-?[0-9]{4}$",message='لطفا شماره خود را وارد کنید . مثال: 09000000000')
money_regex = RegexValidator("^[1-9]\d*$", message="لطفا مقدار پول را به تومان وارد کنید")

class NewUser(AbstractUser):
    address = models.TextField()
    phone_number = models.CharField(validators=[mobile_regex], max_length=15)
    def __str__(self):
        return self.username

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Guarantee(models.Model):
    guarantee_length = models.CharField(max_length=50)
    def __str__(self):
        return self.guarantee_length

class Color(models.Model):
    color = models.CharField(max_length=50)
    def __str__(self):
        return self.color
    
    
class Article(models.Model):
    owner = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    amount = models.BigIntegerField(validators=[money_regex])
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    guraantee = models.ForeignKey(Guarantee, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

