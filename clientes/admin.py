from django.contrib import admin
from .models import Person
from .models import Document

# Register your models here.

admin.site.register(Person)
admin.site.register(Document)
