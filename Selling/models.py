from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

#class Fournisseur 
class Provider(models.Model):
    #les attributs 
    serial_number = models.TextField(max_length=100)
    name = models.TextField(max_length=100)
    firstname = models.TextField(max_length= 100)
    email = models.EmailField()
    tel_number = models.TextField(max_length=25)


#class client
class Customer(models.Model):
    #les attributs 
    name = models.TextField(max_length=100)
    email = models.EmailField()
    tel_number = models.TextField(max_length=25)
    adress = models.TextField()


#class categorie de produits 
class Category (models.Model):
    #les attributs 
    wording = models.TextField(max_length = 100)
    description = models.TextField()


#class des produits 
class Product(models.Model):
    #les attributs 
    name = models.TextField(max_length=100)
    unit_price = models.IntegerField()
    initial_quantity = models.IntegerField()
    #les relations many to one avec ccaregorie et client 
    customer = models.ForeignKey(to = Customer, on_delete = models.DO_NOTHING)
    category = models.ForeignKey(to=Category , on_delete=models.DO_NOTHING)


#class commandes
class Ordered(models.Model):
    #les attributs 
    ordered_number = models.TextField(max_length=50)
    order_quantity = models.IntegerField()
    
# la classe intermediaire de la relation many to many entre commande et produit 
class ProductOrdered(models.Model):
    product = models.ForeignKey(to = Product ,on_delete=models.DO_NOTHING)
    ordered = models.ForeignKey(to = Ordered ,on_delete=models.DO_NOTHING)
    date_ordered = models.DateField(auto_now_add = True)
