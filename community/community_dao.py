from community.models import Community, CommunityMembers, CommunityQam
from constants.community import COMMUNITY_MEMBER_STATUS, COMMUNITY_QAM_STATUS, COMMUNITY_STATUS
from helper.common_helper import CommonHelper
from django.core.paginator import Paginator


class CommunityDao(object):
    page_size = 10

    @staticmethod
    def create_community(name, logo):
        community = Community()
        community.name = name
        if logo:
            community.logo = logo
        community.save()
        _community = CommunityDao.get_community_by_name(name)
        return _community

    @staticmethod
    def get_community_by_id(community_id, user_id):
        if not community_id or not user_id:
            return None
        try:
            community = Community.objects.get(id=community_id)
        except Community.DoesNotExist:
            return None

        if not CommunityDao.is_community_member:
            return None

        return CommunityDao.community_json(community)

    @staticmethod
    def get_community_by_name(name):
        if not name:
            return None
        try:
            community = Community.objects.get(name=name, status=COMMUNITY_STATUS.ACTIVE)
        except Community.DoesNotExist:
            return None
        return CommunityDao.community_json(community)

    @staticmethod
    def get_all_communities(page=1, page_size=10):
        paginator = Paginator(Community.objects.all(), page_size)
        paged_communities = paginator.page(page)
        has_next = page < paginator.num_pages
        _communities = []
        for community in paged_communities:
            _communities.append(CommunityDao.community_json(community))
        return _communities, has_next

    @staticmethod
    def is_community_member(user_id, community_id):
        return CommunityMembers.objects.filter(user_id=user_id, community_id=community_id,
                                               status=COMMUNITY_MEMBER_STATUS.ACTIVE).exist()

    @staticmethod
    def get_community_members(community_id, status, page, page_size=10):
        paginator = Paginator(CommunityMembers.objects.filter(community_id=community_id, status=status), page_size)
        paged_community_members = paginator.page(page)
        has_next = page < paginator.num_pages
        _community_members = []
        for cm in paged_community_members:
            _community_members.append(CommunityDao.community_member_json(cm))
        return _community_members, has_next

    @staticmethod
    def get_community_qams(community_id):
        qams = CommunityQam.objects.filter(community_id=community_id, status=COMMUNITY_QAM_STATUS.ACTIVE)
        _qams = []
        for qam in qams:
            _qams.append(CommunityDao.community_qam_json(qam))
        return _qams

    @classmethod
    def community_json(cls, community, id_required=True):
        community_json = {"id": community.id, "name": community.name, "logo": str(community.logo),
                          "created_at": CommonHelper.from_db_datetime_to_datetime(community.created_at,
                                                                                  "%Y-%m-%d", to_str=True)}
        return community_json

    @classmethod
    def community_member_json(cls, community_member):
        community_member_json = {"name": community_member.user.name,
                                 "role": community_member.role}
        return community_member_json

    @classmethod
    def community_qam_json(cls, qam):
        qam_json = {"title": qam.title,
                    "link": qam.link}
        return qam_json
