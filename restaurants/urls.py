from django.urls import path
from . import views

app_name = 'restaurants'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:restaurant_id>/', views.detail, name='detail'),
    path('<int:restaurant_id>/delete/', views.delete, name='delete'),
    path('<int:restaurant_id>/menu/', views.menu, name='menu'),
    path('<int:restaurant_id>/menu/<int:menu_id>/delete', views.menu_delete, name='menu_delete'),
    path('<int:restaurant_id>/wish/', views.wish, name='wish'),
    path('category/<str:restaurant_category>/', views.category, name='category'),
    path('eatdeal/', views.eatdeal, name='eatdeal'),
    path('region/<str:restaurant_region>/', views.region, name='region')
]