from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='clientes')

    def fullName(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.fullName()
        
