from django.contrib import admin
from .models import Student, Feedback


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'grade']
    search_fields = ['name', 'grade']
    list_filter = ['grade']
    ordering = ['gender', 'grade']


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['text', 'created_at']
    search_fields = ['text']
    ordering = ['-created_at']
    list_filter = ['created_at']
