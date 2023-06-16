from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from community.community_dao import CommunityDao


class CreateCommunityV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(CreateCommunityV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data
        title = self.request.POST.get('name')
        link = self.request.FILES.get('logo')
        community_id = self.request.FILES.get('community_id')
        CommunityDao.create_community_qam(community_id, title, link)
        data = {"success": True, "message": "QAM created successfully"}
        return data
