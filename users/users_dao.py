from users.models import Users
from helper.common_helper import CommonHelper


class UsersDao(object):

    @staticmethod
    def get_user_by_phone(phone):
        if not phone:
            return None
        user = Users.objects.get(phone=phone)
        return UsersDao.post_json(user)

    @classmethod
    def post_json(cls, user):
        post_json = {"name": user.name,
                     "email": user.email,
                     "phone": user.phone,
                     "created_at": CommonHelper.from_db_datetime_to_datetime(user.created_at, "%Y-%m-%d", to_str=True)
                     }
        return post_json
