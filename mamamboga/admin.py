from django.contrib import admin

# Register your models here.
from .models import MamaMboga
class MamaMbogaAdmin(admin.ModelAdmin):
    dislpay_list=("name","email","phonenumber","location","password")
admin.site.register(MamaMboga,MamaMbogaAdmin)