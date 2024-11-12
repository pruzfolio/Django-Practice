from django.urls import path
from . import views

urlpatterns = [
    path('', views.forums, name='forums'),
    path('create/', views.create_post, name='create_post'),  # for create post
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # see post detail
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),  # for like
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),  # for coment sec
]
