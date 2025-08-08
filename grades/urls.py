from django.urls import path
from .views import index, feedback_view, thanks_view, students_view

urlpatterns = [
    path('', index, name='index'),

    path('feedback/', feedback_view, name='feedback'),
    path('thanks/', thanks_view, name='thanks'),
    path('natega/', students_view, name='get_students'),
]
