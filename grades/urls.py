from django.urls import path
from .views import students_view, index

urlpatterns = [
    path('', index, name='index'),
    path('grades/', students_view, name='get_students'),
]
