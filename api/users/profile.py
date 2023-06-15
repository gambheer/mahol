from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from users.users_dao import UsersDao


class ProfileV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(ProfileV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data

        data['user'] = UsersDao.post_json(user)
        return data
