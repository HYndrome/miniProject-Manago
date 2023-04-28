from django.urls import path
from . import views

app_name = 'restaurants'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:restaurant_id>/', views.detail, name='deatil'),
    path('<int:restaurant_id>/likes/', views.likes, name='likes'),
    path('category/<char:restaurant_category>/', views.category, name='category'),
    path('eatdeal/', views.eatdeal, name='eatdeal'),
    path('region/<char:restaurant_address>/', views.region, name='region')
]