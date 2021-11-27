from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.Uzivatel)
admin.site.register(models.Instituce)
admin.site.register(models.Obdarovany)