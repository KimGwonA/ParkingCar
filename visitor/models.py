from datetime import datetime

from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Visitor(models.Model):
    # id = models.BigAutoField(help_text="Visitor ID", primary_key=True)
    carNumber = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    phoneNumber = PhoneNumberField(verbose_name='휴대폰 번호', blank=True, null=True, region='KR')
    carIn = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.carNumber

class Exit(models.Model):
    #visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE)
    id = models.BigAutoField(help_text="Exit ID", primary_key=True)
    visitor_id = models.IntegerField()
    visitor_exit = models.DateTimeField(auto_now_add=True)



# class Exit(models.Model):
#     id = models.BigAutoField(help_text="Exit ID", primary_key=True)
#     visitor_id = models.ForeignKey(Visitor, on_delete=models.CASCADE)  # Visitor의 id만 가지고 온다
#     visitor_exit = models.DateTimeField(auto_now_add=True)