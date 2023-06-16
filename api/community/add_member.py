from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from helper.community_helper import CommunityHelper


class AddMemberV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(AddMemberV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data
        request_body = self.request.req_body
        user_id = self.get_sanitized_int(request_body.get('user_id'))
        community_id = self.get_sanitized_int(request_body.get('community_id', 12))
        CommunityHelper.add_member(user_id, community_id)
        data = {"success": True, "message": "Member added successfully"}
        return data
