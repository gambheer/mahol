class CommunityStatus(object):
    ACTIVE = 1
    INACTIVE = 0
    NEW = 2


class CommunityMemberStatus(object):
    INACTIVE = 0
    ACTIVE = 1
    REQUESTED = 2

    
class CommunityMemberRoles(object):
    ADMIN = 1
    MEMBER = 2


class CommunityQamStatus(object):
    INACTIVE = 0
    ACTIVE = 1


class CommunityPostImages(object):
    IMAGES = ['https://mahol.s3.ap-south-1.amazonaws.com/Greeting/1.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/3.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/4.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/6.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/7.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/8.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/9.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/14.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/Priya.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/Rohit.png']


class CommunityPostVideos(object):
    IMAGES = ['https://mahol.s3.ap-south-1.amazonaws.com/Greeting/1.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/3.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/4.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/6.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/7.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/8.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/9.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/14.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/Priya.png',
              'https://mahol.s3.ap-south-1.amazonaws.com/Greeting/Rohit.png']


COMMUNITY_STATUS = CommunityStatus()
COMMUNITY_MEMBER_STATUS = CommunityMemberStatus()
COMMUNITY_MEMBER_ROLES = CommunityMemberRoles()
COMMUNITY_QAM_STATUS = CommunityQamStatus()
COMMUNITY_POST_IMAGES = CommunityPostImages()
