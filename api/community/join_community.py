from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from helper.community_helper import CommunityHelper


class JoinCommunityV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(JoinCommunityV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data

        community_id = self.get_sanitized_int(self.request.POST.get('community_id'))
        if not community_id:
            data = {"success": False, "message": "Invalid Params"}
            return data

        success, message = CommunityHelper.join_community(user.id, community_id)
        data['success'] = success
        data['message'] = message
        return data
