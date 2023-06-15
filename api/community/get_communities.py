from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from community.models import Community


class GetCommunitiesV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(GetCommunitiesV1, self).__init__(**kwargs)
        self.allowed_methods = ('GET',)

    @allowed_methods
    def get_or_create_data(self):
        data = {}
        communities = Community.objects.all()
        data['communities'] = communities
        return data
