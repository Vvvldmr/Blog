from django.urls import path

from .views import main_page_view, get_post_list, post_detail, create_post, update_post, delete_post


urlpatterns = [
    path('', main_page_view, name='main_page_view'),
    path('posts/', get_post_list, name='post_list'),
    path('posts/<int:post_id>', post_detail, name='post_detail'),
    path('posts/add', create_post, name='create_post'),
    path('posts/<int:post_id>/edit', update_post, name='update_post'),
    path('posts/<int:post_id>/delete', delete_post, name='delete_post')
]