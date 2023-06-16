from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from helper.post_helper import PostHelper


class CreatePostV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(CreatePostV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data

        request_body = self.request.req_body
        community_id = self.get_sanitized_int(request_body.get('community_id'))

        if not community_id:
            data = {"success": False, "message": "Invalid Params"}
            return data

        title = request_body.get('title', "Why it is raining today.")
        _type = request_body.get('type',  'text')
        description = request_body.get('description', "Raining effect is in all over india")
        PostHelper.create_post(community_id, title, _type, description, user.id)

        data = {"success": True, "message": "Post created successfully"}
        return data
