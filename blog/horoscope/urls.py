from django.urls import path
from .views import *

urlpatterns = [
    path('/<int:zodiak>/', get_info_as_number, name="horoscope_number"),
    path('/<str:zodiak>/', get_info, name="horoscope_sign"),
]