from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="main_menu"),
    path('types/', show_types, name="horoscope_types"),
    path('types/<str:elements>', show_type, name="horoscope_category"),
    path('<int:zodiak>/', get_info_as_number, name="horoscope_number"),
    path('<str:zodiak>/', get_info, name="horoscope_sign"),

]