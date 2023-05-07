from django.urls import path
from . import views

app_name = 'clndr'
urlpatterns = [
    path('', views.main, name='main'),
    path('meet/', views.meet, name='meet'),
    path('<str:urlDate>/', views.detail, name='detail'),
    path('<int:meet_id>/attend/', views.attend, name='attend'),
    path('<int:meet_id>/detail/',views.meet_detail, name='meet_detail'),
    path('<int:meet_id>/delete/', views.delete, name='delete')
]