from django.db import models

# POJISTOVACI PRODUKT ( jeho Venue):

class Product(models.Model):
    product_name = models.CharField(max_length=120)
    def __str__(self):
        return self.product_name

# CONTRACT ( jeho Event  )



class Contract(models.Model):

    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.CASCADE)
    amount = models.CharField(max_length=120)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()



# MY CLUB USER:
class Users(models.Model):
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField('User Email')
    address = models.CharField(max_length=240, null=True)
    phone = models.CharField(max_length=100)

    #smlouva = models.ForeignKey(Contract, blank=True, null=True, on_delete=models.CASCADE)
    smlouva = models.ManyToManyField(Contract, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


