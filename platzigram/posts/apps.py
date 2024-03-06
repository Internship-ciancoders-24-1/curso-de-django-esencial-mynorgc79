""" posts aplications module. """
from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"

    """ posts aplication settings """
    name = "posts"
    verbose_name = 'Posts'
