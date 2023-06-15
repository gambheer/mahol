from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from community.community_dao import CommunityDao
from constants.community import COMMUNITY_MEMBER_STATUS


class GetMembersV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(GetMembersV1, self).__init__(**kwargs)
        self.allowed_methods = ('GET',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data

        community_id = self.get_sanitized_int(self.request.GET.get('community_id'))
        status = self.get_sanitized_int(self.request.GET.get('status', COMMUNITY_MEMBER_STATUS.ACTIVE))
        page = self.get_sanitized_int(self.request.GET.get('page', 1))

        community = CommunityDao.get_community_by_id(community_id, user.id)
        if not community:
            data = {"success": False, "message": "Invalid Community"}
            return data

        data['community'] = community

        members, has_next = CommunityDao.get_community_members(community_id, status, page)
        data['members'] = members
        data['has_next'] = has_next
        return data
