from django.urls import path
from blog.views import index, post, page
app_name = 'blog'
urlpatterns = [
    path('', index, name='blog'),
    path('post/', post, name='post'),
    path('page/', page, name='page'),
]
