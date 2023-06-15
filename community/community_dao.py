from community.models import Community
from helper.common_helper import CommonHelper

class CommunityDao(object):

    @staticmethod
    def get_community_by_id(community_id):
        if not id:
            return None
        community = Community.objects.get(id=community_id)
        return CommunityDao.community_json(community)

    @staticmethod
    def get_community_by_name(name):
        if not name:
            return None
        community = Community.objects.get(name=name)
        return CommunityDao.community_json(community)

    @staticmethod
    def get_all_communities():
        communities = Community.objects.all()
        _communities = []
        for community in communities:
            _communities.append(CommunityDao.community_json(community))
        return _communities

    @classmethod
    def community_json(cls, community):
        community_json = {"name": community.name,
                          "created_at": CommonHelper.from_db_datetime_to_datetime(community.created_at,
                                                                                  "%Y-%m-%d", to_str=True)}
        return community_json
