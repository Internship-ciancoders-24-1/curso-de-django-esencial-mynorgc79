

from django.contrib import admin
from django.urls import path

from platzigram import views as local_views
from posts import views as posts_views
from . import views




urlpatterns = [
    # path("admin/", admin.site.urls),
    path('hello-world/', views.hello_world),
    path("hi/<str:name>/<int:age>/",views.say_hi),

    path('posts/', posts_views.list_posts),

    

    
]