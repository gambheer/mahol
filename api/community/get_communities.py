from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from community.community_dao import CommunityDao


class GetCommunitiesV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(GetCommunitiesV1, self).__init__(**kwargs)
        self.allowed_methods = ('GET',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data
        page = self.get_sanitized_int(self.request.GET.get('page', 1))
        communities, has_next = CommunityDao.get_all_communities(page)
        data['communities'] = communities
        data['has_next'] = has_next
        return data
