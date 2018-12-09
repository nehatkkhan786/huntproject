from django.urls import path, include
from . import views


urlpatterns = [
    
    path('', views.home, name = 'home' ),
    path('create', views.pro_create, name = 'create'),
    path('<int:product_id>', views.product_detail, name = 'product_detail'), 
    path('<int:product_id>/upvote', views.upvote, name = 'upvote'), 
]
