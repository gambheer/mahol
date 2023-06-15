from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from community.models import Community


class GetCommunityV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(GetCommunityV1, self).__init__(**kwargs)
        self.allowed_methods = ('GET',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        token = self.request.META('token')
        data['token'] = token
        return data

        # community_id = self.get_sanitized_int(self.request.GET.get('community_id'))
        # if not community_id:
        #     data['token'] = token
        #     data['success'] = False
        #     data['message'] = 'Invalid Params'

        return data
