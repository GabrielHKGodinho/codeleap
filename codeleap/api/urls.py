from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostViewSet.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostretrieveUpdateDestroy.as_view(), name='post-update'),
]
