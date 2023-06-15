from users.models import Users
from helper.common_helper import CommonHelper


class UsersDao(object):

    @staticmethod
    def get_user_by_phone(phone):
        if not phone:
            return None
        user = Users.objects.get(phone=phone)
        return UsersDao.post_json(user)

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return None
        return user

    @staticmethod
    def update_profile(user_id, image, name):
        user = UsersDao.get_user_by_id(user_id)
        if not user:
            return None
        user.image = image
        user.name = name
        user.save()
        return UsersDao.post_json(user)

    @classmethod
    def post_json(cls, user):
        post_json = {"name": user.name,
                     "email": user.email,
                     "phone": user.phone,
                     "image": "https://mahol.s3.ap-south-1.amazonaws.com/users/user.png",
                     "created_at": CommonHelper.from_db_datetime_to_datetime(user.created_at, "%Y-%m-%d", to_str=True)
                     }
        return post_json
