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
        name = self.request.POST.get('name')
        logo = self.request.FILES.get('logo')
        if not name:
            data = {"success": False, "message": "Invalid Params"}
            return data

        if CommunityDao.get_community_by_name(name):
            data = {"success": False, "message": "Community already exist"}
            return data

        community = CommunityDao.create_community(name, logo)
        data['community'] = community
        return data
