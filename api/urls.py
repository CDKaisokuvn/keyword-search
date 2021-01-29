from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_api_overview, name='api_overview'),
    path('keywords', views.get_keyword, name='get_keyword')

]
