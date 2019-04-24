from django.db import models

# Create your models here.

class Document(models.Model):
    rg = models.CharField(max_length=12)
    #cpf = models.CharField(max_length=14)
    def __str__(self):
        return self.rg

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    adress = models.CharField(max_length=1500, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='clientes')
    doc = models.OneToOneField(Document, null=True, blank=True, on_delete=models.CASCADE)

    def fullName(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.fullName()
        
