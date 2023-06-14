from django.urls import include, re_path
from .users import urls as user_urls

urlpatterns = [
    re_path('^users/', include(user_urls)),
]
