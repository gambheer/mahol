from api.response.base import APIResponseBase
from api.decorators.validators import allowed_methods
from users.models import Users

class VerifyOtpV1(APIResponseBase):
    __versions_compatible__ = ('1', '1.0')

    def __init__(self, **kwargs):
        super(VerifyOtpV1, self).__init__(**kwargs)
        self.allowed_methods = ('POST',)

    @allowed_methods
    def get_or_create_data(self):
        data = {"success": True}
        request_body = self.request.req_body
        otp = request_body.get('otp')
        phone = request_body.get('phone')
        if not otp or not phone:
            data['success'] = False
            data['message'] = "Invalid Params"
            return data

        try:
            user = Users.objects.get(phone=phone)
        except Users.DoesNotExist:
            data['success'] = False
            data['message'] = "Invalid Phone Number"
            return data

        data['token'] = user.token
        data['message'] = "OTP verified successfully"

        return data
