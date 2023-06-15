from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from . import GetCommunitiesV1
from . import GetCommunityV1

urlpatterns = [
    re_path('^get-communities/$', csrf_exempt(GetCommunitiesV1.as_versioned_view())),
    re_path('^get-community/$', csrf_exempt(GetCommunityV1.as_versioned_view())),
]
