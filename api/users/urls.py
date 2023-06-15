from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from . import GetOtpV1
from . import VerifyOtpV1
from . import ProfileV1

urlpatterns = [
    re_path('^auth/get-otp/$', csrf_exempt(GetOtpV1.as_versioned_view())),
    re_path('^auth/verify-otp/$', csrf_exempt(VerifyOtpV1.as_versioned_view())),
    re_path('^profile/$', csrf_exempt(ProfileV1.as_versioned_view())),
]
