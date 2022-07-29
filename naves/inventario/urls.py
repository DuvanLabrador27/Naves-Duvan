from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('nave/', views.NavesLanzaderas, name='nave'),
    path('navenotripulada/', views.navesNoTripuladas, name='navedos'),
    path('navetripulada/', views.navesTripuladas, name='navetres'),


    

]