from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('<int:restaurant_id>/create/', views.create, name='create'),
    path('<int:restaurant_id>/<int:review_id>/', views.detail, name='detail'),
    path('<int:restaurant_id>/<int:review_id>/delete/', views.delete, name='delete'),
    path('<int:restaurant_id>/<int:review_id>/update/', views.update, name='update'),
    path('<int:restaurant_id>/<int:review_id>/likes/', views.likes, name='likes'),
    path('<int:restaurant_id>/<int:review_id>/comments/', views.comment_create, name='comment_create'),
    path('<int:restaurant_id>/<int:review_id>/comments/<int:comment_id>/delete/', views.comment_delete, name='comment_delete'),
]
