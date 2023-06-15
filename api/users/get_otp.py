from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods


class GetOtpV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(GetOtpV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST',)

    @allowed_methods
    def get_or_create_data(self):
        data = {}
        request_body = self.request.req_body
        phone = request_body.get('phone')
        if not phone:
            data['success'] = False
            data['message'] = "Invalid Phone Number"
            return data

        data['otp'] = 123456
        data['success'] = True
        data['message'] = "OTP sent successfully"

        return data
