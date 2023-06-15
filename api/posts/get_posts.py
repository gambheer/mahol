from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from posts.posts_dao import PostsDao


class GetPostsV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(GetPostsV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data

        _id = self.get_sanitized_int(self.request.GET.get('id'))
        if not _id:
            data = {"success": False, "message": "Invalid Params"}
            return data

        post = PostsDao.get_post_by_id(_id)
        data['post'] = post
        return data
