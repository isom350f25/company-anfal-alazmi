from django.contrib import admin

# Register your models here.

from .models import Employee
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'position')  
    list_filter = ('joined_on',)              
    search_fields = ('name',)  