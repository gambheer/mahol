from django.urls import include, re_path
from .users import urls as user_urls
from .community import urls as community_urls
from .posts import urls as post_urls


urlpatterns = [
    re_path('^users/', include(user_urls)),
    re_path('^community/', include(community_urls)),
    re_path('^posts/', include(post_urls)),
]
