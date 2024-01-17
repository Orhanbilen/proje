from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(("İşler"),max_length=50)
    text = models.TextField()
    date_now = models.DateTimeField(("Tarih - Saat"), auto_now=False, auto_now_add=False)
    author = models.CharField(("Yazar"), max_length=50)
    
class Contact(models.Model):
    fullname = models.CharField(("Ad"), max_length=50) 
    lastname = models.CharField(("SoyAd"), max_length=50, null=True, blank=True)
    email = models.EmailField(("Email"), max_length=254)
    phone = models.CharField(("Telefon"), max_length=100, null=True, blank=True) 
    adress = models.CharField(max_length=255, default='Bilgi yok')

