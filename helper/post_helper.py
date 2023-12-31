import random
from posts.models import Posts, Comments


class PostHelper(object):
    @staticmethod
    def create_post(community_id, title, _type, description, user_id):
        post = Posts()
        post.title = title
        post.user_id = user_id
        post.type = _type
        post.content = PostHelper.get_content_by_type(_type)
        post.description = description
        post.community_id = community_id

        post.save()

    @staticmethod
    def get_content_by_type(_type):
        r = random.randint(1, 10)
        images = ['https://mahol.s3.ap-south-1.amazonaws.com/Greeting/1.png',
                  'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/3.png',
                  'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/4.png',
                  'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/6.png',
                  'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/7.png',
                  'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/8.png',
                  'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/9.png',
                  'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/14.png',
                  'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/Priya.png',
                  'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/Rohit.png']
        if _type == 'image':
            return images[r]
        return None

    @staticmethod
    def create_comment_on_post(user_id, post_id, title, _type, description):
        comment = Comments()
        comment.title = title
        comment.user_id = user_id
        comment.type = _type
        comment.content = PostHelper.get_content_by_type(_type)
        comment.post_id = post_id

        comment.save()