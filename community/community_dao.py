from community.models import Community


class CommunityDao(object):

    @staticmethod
    def get_community_by_id(community_id):
        if not id:
            return None
        community = Community.object.get(id=community_id)
        return CommunityDao.community_json(community)

    @staticmethod
    def get_community_by_name(name):
        if not name:
            return None
        community = Community.object.get(name=name)
        return CommunityDao.community_json(community)

    @staticmethod
    def get_all_communities():
        communities = Community.objects.all()
        _communities = dict()
        for community in communities:
            _communities.update(CommunityDao.community_json(community))
        return _communities

    @classmethod
    def community_json(cls, community):
        communoty_json = {"name": community.name,
                          "created_at": community.created_at}
        return communoty_json
