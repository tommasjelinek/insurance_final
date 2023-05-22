from django.db import models


class Users(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField('User Email')
    address = models.CharField(max_length=240, null=True)


    phone = models.CharField(max_length=100)


    class Meta:
        verbose_name = "uzivatele_pojisteni"

    def __str__(self):
        return self.first_name + ' ' + self.last_name




class Pojisteni(models.Model):
    typy_pojisteni = models.CharField(max_length=240)


    class Meta:
        verbose_name = "Pojisteni"

    def __str__(self):
        return self.typy_pojisteni


