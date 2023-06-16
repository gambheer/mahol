from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from community.community_dao import CommunityDao


class CreateQamV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(CreateQamV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data
        request_body = self.request.req_body
        title = request_body.get('title')
        link = request_body.get('link')
        community_id = request_body.get('community_id')
        CommunityDao.create_community_qam(community_id, title, link)
        data = {"success": True, "message": "QAM created successfully"}
        return data
