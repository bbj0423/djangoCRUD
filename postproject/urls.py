from django.contrib import admin
from django.urls import path
import blogapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/<int:blog_id>/', blogapp.views.detail, name='detail'),
    path('blog/new/', blogapp.views.new, name='new'),
    path('blog/create/', blogapp.views.create, name='create'),
    path('blog/update/<int:blog_id>/', blogapp.views.update, name='update'),
    path('blog/edit/<int:blog_id>/', blogapp.views.edit, name='edit'),
    path('blog/newblog/', blogapp.views.blogpost, name='newblog'),
    path('blog/delete/<int:blog_id>/', blogapp.views.delete, name='delete'),
]
