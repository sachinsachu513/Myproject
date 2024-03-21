from django.db import models


class registration(models.Model):
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    age = models.IntegerField()
    adress=models.CharField(max_length=15)
    emailid=models.EmailField()
    phonenumber=models.IntegerField()
    password=models.CharField(max_length=15)


    def __str__(self):
        return self.first_name