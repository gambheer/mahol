from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from . import GetPostsV1

urlpatterns = [
    re_path('^get-posts/$', csrf_exempt(GetPostsV1.as_versioned_view())),
]
