from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from helper.post_helper import PostHelper


class PostCommentV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(PostCommentV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data
        request_body = self.request.req_body

        post_id = self.get_sanitized_int(request_body.get('post_id'))
        title = request_body.get('title', "Why it is raining today.")
        _type = request_body.get('type', 'text')
        description = request_body.get('description', "Raining effect is in all over india")
        PostHelper.create_comment_on_post(user.id, post_id, title, _type, description)
        data = {"success": True, "message": "Comment created successfully"}
        return data

        return data
