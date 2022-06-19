from django.urls import path
from .views import *

urlpatterns = [
    path('', get_routes, name='routes'),
    path('notas/', get_notes, name='notas'),
    path('notas/<str:pk>/', get_note, name='nota')
]
