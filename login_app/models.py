from django.db import models

# Create your models here.
class deatils(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=25)
    class Meta:
        db_table = 'persons'
    