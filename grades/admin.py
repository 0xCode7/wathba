from django.contrib import admin
from .models import Student


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade']
    search_fields = ['name', 'grade']
    list_filter = ['grade']
    ordering = ['gender', 'grade']
