from django.db import models

# Create your models here.

class Form(models.Model):
    SEX = [
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    ]
    MARITAL_STATUS = [
        ('married', 'married'),
        ('single', 'single'),
        ('divorced', 'divorced'),
        ('other', 'other'),
    ]
    EDUCATION = [
        ('high school', 'high school'),
        ('degree', 'degree'),
        ('masters', 'masters'),
        ('other', 'other'),
    ]
    COUNTRY = [
        ('canada', 'canada'),
        ('uae', 'uae'),
        ('australia', 'australia'),
        ('uk', 'uk'),
        ('germany','germany')
    ]
    PASSPORT=[
        ('yes','yes'),
        ('no','no')
    ]
    
    
    name= models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    telephone = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True)
    province = models.CharField(max_length= 100, null=True)
    dob = models.DateField()
    sex = models.CharField(max_length=20, choices=SEX)
    marital_status = models.CharField(max_length=20, choices=MARITAL_STATUS)
    occupation = models.CharField(max_length=100, null=False)
    education = models.CharField(max_length=20, choices=EDUCATION)
    digital_address = models.CharField(max_length=100, null=False)
    country_from = models.CharField(max_length=100, null=False)
    country_to = models.CharField(max_length=20, choices=COUNTRY)
    passport = models.CharField(max_length=100, choices=PASSPORT, null=True)
    
    # def __str__(self):
    #     return self