from django.urls import path
from . import views
app_name = "core"
urlpatterns = [
    path('posts/', views.PostListCreateView.as_view(), name='post_list_create'),
    path('posts/<int:pk>/', views.PostDetailUpdateDeleteView.as_view(), name='post_detail_update_delete'),
]