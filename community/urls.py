# community/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from community import views

urlpatterns = [
    path("community/", views.CommunityList.as_view()),
    path("community/<int:pk>/", views.CommunityDetail.as_view()),
    path("", views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)