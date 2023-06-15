from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from users.users_dao import UsersDao


class GetUsersV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(GetUsersV1, self).__init__(**kwargs)
        self.allowed_methods = ('GET',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data
        page = self.get_sanitized_int(self.request.GET.get('page', 1))
        users, has_next = UsersDao.get_all_users(page)
        data['users'] = users
        data['has_next'] = has_next
        return data
