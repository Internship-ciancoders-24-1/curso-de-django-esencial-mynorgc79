

from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings
from platzigram import views as local_views
from posts import views as posts_views
from . import views
from users import views as users_views




urlpatterns = [
    path("admin/", admin.site.urls),

    path('hello-world/', views.hello_world),
    path("hi/<str:name>/<int:age>/",views.say_hi),

    path('posts/', posts_views.list_posts),

    path('user/login', users_views.login_view, name='login'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
