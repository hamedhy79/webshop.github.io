from django.contrib import admin
from .models import Customer

# class UserAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'created']


admin.site.register(Customer)
