from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from . import GetPostsV1
from . import PostCommentV1
from . import GetPostCommentsV1
from . import CreatePostV1

urlpatterns = [
    re_path('^get-posts/$', csrf_exempt(GetPostsV1.as_versioned_view())),
    re_path('^create-post/$', csrf_exempt(CreatePostV1.as_versioned_view())),
    re_path('^get-post-comments/$', csrf_exempt(GetPostCommentsV1.as_versioned_view())),
    re_path('^post-comments/$', csrf_exempt(PostCommentV1.as_versioned_view())),
]
