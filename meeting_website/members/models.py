from django.contrib.auth.models import User


from django.db import models

User._meta.get_field('email')._unique = True



class Person(models.Model):
    avatar = models.ImageField(upload_to='avatars', blank=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=254, unique=True, blank=True)

    def __str__(self):
        return self.email
