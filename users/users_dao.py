from users.models import Users
from helper.common_helper import CommonHelper
from django.core.paginator import Paginator


class UsersDao(object):

    @staticmethod
    def get_user_by_phone(phone):
        if not phone:
            return None
        user = Users.objects.get(phone=phone)
        return UsersDao.user_json(user)

    @staticmethod
    def get_user_by_id(user_id):
        try:
            user = Users.objects.get(id=user_id)
        except Users.DoesNotExist:
            return None
        return user

    @staticmethod
    def get_all_users(page=1, page_size=10):
        paginator = Paginator(UsersDao.objects.all(), page_size)
        paged_users = paginator.page(page)
        has_next = page < paginator.num_pages
        _users = []
        for user in paged_users:
            _users.append(UsersDao.user_json(user))
        return _users, has_next

    @staticmethod
    def update_profile(user_id, image, name):
        user = UsersDao.get_user_by_id(user_id)
        if not user:
            return None
        user.image = image
        user.name = name
        user.save()
        return UsersDao.user_json(user)

    @classmethod
    def user_json(cls, user):
        post_json = {"user_id": user.id,
                     "description": "Hello",
                     "name": user.name,
                     "email": user.email,
                     "phone": user.phone,
                     "role": user.role,
                     "department": user.department.name,
                     "image": "https://mahol.s3.ap-south-1.amazonaws.com/users/user.png",
                     "reaction_count": 5,
                     "comment_count": 2,
                     "created_at": CommonHelper.from_db_datetime_to_datetime(user.created_at, "%Y-%m-%d", to_str=True)
                     }
        return post_json
