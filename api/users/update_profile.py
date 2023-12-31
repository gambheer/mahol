from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from users.users_dao import UsersDao


class UpdateProfileV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(UpdateProfileV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data
        request = self.request
        image = request.FILES.get('image')
        name = request.POST.get('name')
        UsersDao.update_profile(user.id, image, name)
        data['user'] = UsersDao.user_json(user)
        return data
