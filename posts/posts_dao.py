from posts.models import Posts


class PostsDao(object):

    @staticmethod
    def get_post_by_id(post_id):
        if not id:
            return None
        post = Posts.object.get(id=post_id)
        return PostsDao.post_json(post)

    @staticmethod
    def get_community_by_title(title):
        if not title:
            return None
        post = Posts.object.get(title=title)
        return PostsDao.community_json(post)

    @staticmethod
    def get_all_communities():
        posts = Posts.objects.all()
        _posts = dict()
        for post in posts:
            _posts.update(PostsDao.post_json(post))
        return _posts

    @classmethod
    def post_json(cls, post):
        post_json = {"title": post.title,
                     "description": post.description,
                     "created_at": post.created_at}
        return post_json
