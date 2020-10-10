from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home-page'),
    path('dashboard', views.dashboard, name='dashboard-page'),
    path('maps_google', views.maps_google, name='maps-page'),
    path('page_404', views.page404, name='404-page'),
]
