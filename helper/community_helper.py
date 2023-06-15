from community.models import CommunityMembers
from community.community_dao import CommunityDao
from constants.community import COMMUNITY_MEMBER_STATUS


class CommunityHelper(object):

    @staticmethod
    def join_community(user_id, community_id):
        if not CommunityDao.get_community_by_id(community_id):
            return False, "Invalid Community"

        if CommunityDao.is_community_member(user_id, community_id):
            return False, "Already a member of this community"

        member = CommunityMembers()
        member.user_id = user_id
        member.community_id = community_id
        member.status = COMMUNITY_MEMBER_STATUS.REQUESTED
        member.save()
        return True, "Request sent for approval."
