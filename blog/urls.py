from django.urls import path

from blog.views import categories, posts, tags

app_name = 'blog'

urlpatterns = [
    # posts
    path('posts/', posts.post_list, name='post_list'),
    path('posts/<slug:slug>/', posts.post_detail, name='post_detail'),
    # category
    path('categories/<slug:slug>/', categories.posts_by_category, name='posts_by_category'),
    # tags
    path('tags/<slug:tag_slug>/', tags.posts_by_tag, name='posts_by_tag'),
]
