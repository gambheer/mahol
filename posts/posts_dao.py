from posts.models import Posts
from django.core.paginator import Paginator
from helper.common_helper import CommonHelper


class PostsDao(object):

    @staticmethod
    def get_post_by_id(post_id):
        if not id:
            return None
        post = Posts.objects.get(id=post_id)
        return PostsDao.post_json(post)

    @staticmethod
    def get_posts_by_community_id(community_id, page=1, page_size=10):
        if not community_id:
            return None
        paginator = Paginator(Posts.objects.filter(community_id=community_id).order_by('created_on'), page_size)
        paged_posts = paginator.page(page)
        has_next = page < paginator.num_pages
        _posts = []
        for post in paged_posts:
            _posts.append(PostsDao.post_json(post))
        return _posts, has_next

    @classmethod
    def post_json(cls, post):
        post_json = {"title": post.title,
                     "description": post.description,
                     "type": post.type,
                     "content": post.content,
                     "created_at": CommonHelper.from_db_datetime_to_datetime(post.created_at, '%Y-%m-%d', to_str=True)}
        return post_json
