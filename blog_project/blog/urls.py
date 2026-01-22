from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('signup/', views.signup, name='signup'),
    path("post/new/", views.create_post, name="create-post"),
    path('post/<int:post_id>/edit/', views.edit_post, name='edit-post'),
    path('post/<int:post_id>/delete/', views.delete_post, name='delete-post'),
]
