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


COMMUNITY_STATUS = CommunityStatus()
COMMUNITY_MEMBER_STATUS = CommunityMemberStatus()
COMMUNITY_MEMBER_ROLES = CommunityMemberRoles()
COMMUNITY_QAM_STATUS = CommunityQamStatus()
