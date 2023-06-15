from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from . import GetOtpV1

urlpatterns = [
    re_path('^communities/$', csrf_exempt(GetOtpV1.as_versioned_view())),
    re_path('^community/$', csrf_exempt(GetOtpV1.as_versioned_view())),
]
