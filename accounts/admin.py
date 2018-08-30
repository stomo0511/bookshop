from django.contrib import admin

# Register your models here.
# 20180830 18:46
from .models import CustomUser

admin.site.register(CustomUser)

# OK