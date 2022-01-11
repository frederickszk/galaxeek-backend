from django.urls import path
from api import views
from api import views_iot
from api import views_user

urlpatterns = [
    path('position_list', views.position_list),
    path('devices', views.devices),
    path('positions', views.positions),

    path('iot/positions', views_iot.positions),
    path('iot/action', views_iot.action),

    path('user/login', views_user.login),

]