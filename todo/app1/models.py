from django.contrib.auth.models import User
from django.db import models

class Reja(models.Model):
    sarlavha=models.CharField(max_length=50)
    vaqti=models.DateTimeField()
    malumot=models.CharField(max_length=200)
    status=models.CharField(max_length=50, choices=(("bajarildi","bajarildi"),("bajarilgani yoq","bajarilgani yoq")))
    foydalanuvchi=models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.sarlavha