from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from posts.posts_dao import PostsDao


class GetPostCommentsV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(GetPostCommentsV1, self).__init__(**kwargs)
        self.allowed_methods = ('GET',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        user = self.get_user(self.request.META.get('HTTP_AUTHORIZATION'))
        if not user:
            data = {"success": False, "message": "Invalid User"}
            return data

        post_id = self.get_sanitized_int(self.request.GET.get('post_id'))
        page = self.get_sanitized_int(self.request.GET.get('page', 1))
        if not post_id:
            data = {"success": False, "message": "Invalid Params"}
            return data

        comments, has_next = PostsDao.get_post_comments(post_id, page)
        data['comments'] = comments
        data['has_next'] = has_next
        return data
