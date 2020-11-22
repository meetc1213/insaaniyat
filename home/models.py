from django.db import models

# Create your models here.
class donors(models.Model):
    """docstring for profile."""
    # extra fields
    # clubimage=models.ImageField(upload_to='logos/')
    name = models.TextField(blank=False)
    gender=models.TextField(blank=False)
    bloodgroup=models.TextField(blank=False)
    date_pos=models.TextField(blank=False)
    date_neg=models.TextField(blank=False)
    email=models.TextField(blank=False)
    phone=models.TextField(blank=False)
    city=models.TextField(blank=False)
    exist_cond=models.TextField(blank=False)
    def __str__(self):
        return self.name
class recipient(models.Model):
    """docstring for profile."""
    # extra fields
    # clubimage=models.ImageField(upload_to='logos/')
    name = models.TextField(blank=False)
    gender=models.TextField(blank=False)
    bloodgroup=models.TextField(blank=False)
    hospital=models.TextField(blank=False)
    amt_needed=models.TextField(blank=False)
    email=models.TextField(blank=False)
    phone=models.TextField(blank=False)
    city=models.TextField(blank=False)
    exist_cond=models.TextField(blank=False)
    def __str__(self):
        return self.name