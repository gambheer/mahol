import uuid
from users.models import Users


class AuthHelper(object):

    @staticmethod
    def authenticate_user(token):
        return

    @staticmethod
    def get_token_by_phone(phone):
        return

    @staticmethod
    def get_user_by_token(token):
        return

    @staticmethod
    def get_or_create_user(phone):
        try:
            user = Users.objects.get(phone=phone)
        except Users.DoesNotExist:
            user = Users()
            user.phone = phone
            user.token = str(uuid.uuid1())
            user.save()
        return user


