from django.contrib import admin
from django.urls import path

from todolist.views import todo, category, redirect_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_view),
    path('todo/', todo, name='todo_list'),
    path('category/', category, name='category'),
]
