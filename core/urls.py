from django.urls import path
from .views import *

app_name ='core'

urlpatterns = [
    path('login/',login_page,name='login'),
    path("logout/",logout_page, name="logout"),
    path('index/',index,name='index'),
    path("index/stat/province", stat_province, name="stat_province"),
    path("index/stat/zone", stat_zone, name="stat_zone"),
    path("index/stat/aire", stat_aire, name="stat_aire"),
    path('index/province/list/',province_list,name='province_list'),
    path("index/provine/add/",province_create, name="province_create"),
    path("index/province/<int:pk>/update/", province_update, name="province_update"),
    path('index/zone-sanitaire/list/',zone_sanitaire_list,name='zone_sanitaire_list'),
    path("index/zone-sanitaire/add/", zone_sanitaire_create, name="zone_sanitaire_create"),
    path("index/zone-sanitaire/<int:pk>/update/", zone_sanitaire_update, name="zone_sanitaire_update"),
    path('index/aire-sanitaire/list/',aire_sanitaire_list,name='aire_sanitaire_list'),
    path("index/aire-sanitaire/add/", aire_sanitaire_create, name="aire_sanitaire_create"),
    path("index/aire-sanitaire/<int:pk>/update", aire_sanitaire_update, name="aire_sanitaire_update"),
]

