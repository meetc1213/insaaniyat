from django.contrib import admin
from home.models import recipient,donors
# Register your models here.

admin.site.register(donors)
admin.site.register(recipient)