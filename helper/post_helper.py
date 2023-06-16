import random
from constants.community import COMMUNITY_POST_IMAGES
from posts.models import Posts


class PostHelper(object):
    @staticmethod
    def create_post(community_id, title, _type, description):
        post = Posts()
        post.title = title
        post.type = _type
        post.content = PostHelper.get_content_by_type(_type)
        post.description = description
        post.community_id = community_id

        post.save()

    @staticmethod
    def get_content_by_type(_type):
        r = random.randint(1, 10)
        if _type == 'image':
            return COMMUNITY_POST_IMAGES[r]
        return None


