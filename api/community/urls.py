from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from . import GetCommunitiesV1
from . import GetCommunityV1
from . import CreateCommunityV1
from . import JoinCommunityV1
from . import AddMemberV1
from . import GetMembersV1

urlpatterns = [
    re_path('^get-communities/$', csrf_exempt(GetCommunitiesV1.as_versioned_view())),
    re_path('^get-community/$', csrf_exempt(GetCommunityV1.as_versioned_view())),
    re_path('^create-community/$', csrf_exempt(CreateCommunityV1.as_versioned_view())),
    re_path('^join-community/$', csrf_exempt(JoinCommunityV1.as_versioned_view())),
    re_path('^add-member/$', csrf_exempt(AddMemberV1.as_versioned_view())),
    re_path('^get-members/$', csrf_exempt(GetMembersV1.as_versioned_view())),
]
