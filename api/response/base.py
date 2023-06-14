import json
import uuid
from functools import update_wrapper
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.utils.decorators import classonlymethod
from django.views.generic.base import View


class APIResponseBase(View):
    """
    Base class for all API responses
    """

    __versions_compatible__ = ('1', '1.0')
    __page_size__ = 10

    template_name = None

    @classonlymethod
    def as_versioned_view(cls, **initkwargs):
        """
        Main entry point for a request-response process.
        """
        # sanitize keyword arguments
        for key in initkwargs:
            if key in cls.http_method_names:
                raise TypeError(u"You tried to pass in the %s method name as a "
                                u"keyword argument to %s(). Don't do that."
                                % (key, cls.__name__))
            if not hasattr(cls, key):
                raise TypeError(u"%s() received an invalid keyword %r" % (
                    cls.__name__, key))

        def view(request, *args, **kwargs):
            # Get version from kwargs
            _v = kwargs.get('_v')
            self = None
            log.debug("Pvs: version: {}".format(_v))
            if _v:
                # If version is present, find the subclasses which serve this version
                # Initialize the first one which serves this version.
                # Need to enforce discipline of avoiding version conflicts
                # We only look for first level subclasses, can extend in loop if necessary
                for sub_cls in cls.all_subclasses():
                    if sub_cls.satisfies_version(_v):
                        self = sub_cls(**initkwargs)
                        break
            # Fall back to the base class provided if no matching version is found
            if not self:
                self = cls(**initkwargs)
            if hasattr(self, 'get') and not hasattr(self, 'head'):
                self.head = self.get
            self.request = request
            self.args = args
            self.kwargs = kwargs
            return self.dispatch(request, *args, **kwargs)

        # take name and docstring from class
        update_wrapper(view, cls, updated=())

        # and possible attributes set by decorators
        # like csrf_exempt from dispatch
        update_wrapper(view, cls.dispatch, assigned=())
        return view

    @classonlymethod
    def satisfies_version(cls, _v):
        return _v in cls.__versions_compatible__

    @classonlymethod
    def all_subclasses(cls):
        all_subclasses = []
        for subclass in cls.__subclasses__():
            all_subclasses.append(subclass)
            all_subclasses.extend(subclass.all_subclasses())
        return all_subclasses

    def __init__(self, **kwargs):
        super(APIResponseBase, self).__init__(**kwargs)

        self._context = None
        self._header_context = None
        self.request_id = str(uuid.uuid4())
        self._data = {}

        self.include_header = False

        self.status = 'success'
        self.status_code = 200
        self.message = ''
        self.error_code = ''
        self.error_message = ''
        # Set this as True to get raw response
        self.exempt_json = False
        self.content_type = "application/json"

        self.redirect_to = None

        self.cookie_key = None
        self.cookie_value = None
        self.cookie_expires = None

    def get_request(self):
        return self.request

    def get_profile(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            if not user.has_premium and self.is_user_marked_premium_for_authorized_order(user.id):
                user.has_premium = True
            return user
        return None

    def get_request_args(self):
        return self.args

    def get_request_kwargs(self):
        return self.kwargs

    def get_param(self, p):
        r = self.get_request()
        if r.method == 'POST':
            return r.POST.get(p,'').strip()
        if r.method == 'GET':
            return r.GET.get(p,'').strip()

    def get_param_list(self, p):
        r = self.get_request()
        if r.method == 'POST':
            return r.POST.getlist(p)
        if r.method == 'GET':
            return r.GET.getlist(p)

    def render_to_response(self, **response_kwargs):
        """
        Returns a HttpResponse with jsonized context.
        """

        self.before_creating_context()

        _context = {}
        if self.update_request_body():
            if self.is_user_suspended():
                self.set_suspended_user()
            elif hasattr(self.request, 'token_unique_id') and (not self.is_token_active()):
                pass
            else:
                _context.update(self.get_or_create_context())

        if self.message:
            _context['message'] = self.message
        if self.error_code:
            _context['error_code'] = self.error_code
        if self.error_message:
            _context['error_message'] = self.error_message

        if self.status_code == 302:
            return HttpResponseRedirect('%s' % self.redirect_to)
        elif self.status_code == 301:
            return HttpResponsePermanentRedirect('%s' % self.redirect_to)

        if not self.exempt_json:
            if self.status_code == 456:
                response = HttpResponse(json.dumps(_context), content_type=self.content_type, status=self.status_code,
                                        reason=self.error_message)
            else:
                response = HttpResponse(json.dumps(_context), content_type=self.content_type, status=self.status_code)
        else:
            response = HttpResponse(_context.get("raw_data", ""), content_type=self.content_type,
                                    status=self.status_code)

        if self.request.META.get('HTTP_CACHE_CONTROL'):
            response['Cache-Control'] = self.request.META.get('HTTP_CACHE_CONTROL')

        if self.cookie_key and self.cookie_value and self.cookie_expires:
            response.set_cookie(key=self.cookie_key, value=self.cookie_value, expires=self.cookie_expires, secure=True)

        return response

    def before_creating_context(self):
        """
        Hook to write code to initiliaze/process before creating context
        """
        self.add_request_source()
        self.update_url_kwargs()
        self.add_utm_source()
        self.update_user_country_cache()
        pass

    def get_or_create_context(self):
        """
        Returns context. If context is not created,
        it creates and returns it
        """
        if self._context:
            return self._context

        _context = {}
        self._context = _context

        self.add_data_to_context()
        #self.add_header_to_context()
        self.on_context_created()

        return self._context

    def add_header_to_context(self):
        if self.request.include_header or self.include_header:
            self._context['header'] = self.get_or_create_header_context()

    def add_data_to_context(self):
        data = self.get_or_create_data()
        if data and type(data) is dict:
            self._context.update(data)
        else:
            self._context.update({"raw_data": data})

    def on_context_created(self):
        """
        Hook to write code to process created context
        """
        pass

    def get_or_create_data(self):
        """
        Method which should be overridden/implemented by derived views
        to get the data specific to API
        """
        return self._data

    def get_or_create_header_context(self):
        """
        Returns header context. If header context is not created
        it creates and returns it
        """
        if self._header_context:
            return self._header_context

        _context = {}
        self._header_context = _context

        self.on_header_context_created()

        return self._header_context

    def on_header_context_created(self):
        """
        Hook to adjust header context's user and course contexts
        based on each other
        """
        pass

    def update_request_body(self):
        request = self.request
        request.req_body = {}
        success = True
        if request.method == 'POST' and request.content_type == 'application/json' and request.body:
            try:
                request.req_body = json.loads(request.body.decode('utf-8'))
            except:
                success = False
                self.set_bad_req('Corrupt JSON body in request.', 'INVALID_JSON_BODY')
        return success

    def get(self, request, *args, **kwargs):
        return self.render_to_response()

    def post(self, request, *args, **kwargs):
        return self.render_to_response()

    def head(self, request, *args, **kwargs):
        return self.render_to_response()

    def put(self, request, *args, **kwargs):
        return self.render_to_response()

    def trace(self, request, *args, **kwargs):
        return self.render_to_response()

    def options(self, request, *args, **kwargs):
        return self.render_to_response()

    def delete(self, request, *args, **kwargs):
        return self.render_to_response()

    def set_success(self, msg=''):
        self.status = 'success'
        self.status_code = 200
        self.message = msg

    def set_redirect(self, redirect_to, permanent=False):
        self.status_code = 301 if permanent else 302
        self.redirect_to = redirect_to
        self.status = 'redirect'

    def set_bad_req(self, msg, error_code):
        self.status = 'failed'
        self.status_code = 400
        self.error_message = msg
        self.error_code = error_code

    def set_401(self):
        self.status = 'error'
        self.status_code = 401
        self.message = 'Login required to access this resource'

    def set_403(self):
        self.status = 'error'
        self.status_code = 403
        self.message = 'You do not have permission access this resource'

    def set_500(self):
        self.status = 'error'
        self.status_code = 500
        self.message = 'Something went wrong'

    def set_suspended_user(self):
        self.status = 'error'
        self.status_code = 403
        self.error_message = 'Your account has been suspended'
        self.error_code = 'SUSPENDED_USER'

    def set_404(self, msg, error_code):
        self.status = 'failed'
        self.status_code = 404
        self.error_message = msg
        self.error_code = error_code

    def set_503(self, msg, error_code):
        self.status = 'failed'
        self.status_code = 503
        self.error_message = msg
        self.error_code = error_code

    def set_precondition_failed(self, msg, error_code):
        self.status = 'failed'
        self.status_code = 412
        self.error_message = msg
        self.error_code = error_code

    def set_unsupported_method(self, msg, error_code):
        self.status = 'failed'
        self.status_code = 405
        self.error_message = msg
        self.error_code = error_code

    def set_payload_too_large(self, msg):
        self.status = 'failed'
        self.status_code = 413
        self.error_message = msg

    def set_error(self, msg, error_code):
        self.status = 'failed'
        self.status_code = 500
        self.error_message = msg
        self.error_code = error_code

    def set_cookie(self, key, value, expires):
        self.cookie_key = key
        self.cookie_value = value
        self.cookie_expires = expires

    @staticmethod
    def get_sanitized_int(data):
        try:
            data = int(data)
            return data
        except:
            return None

    @staticmethod
    def get_sanitized_int_list(data):
        int_list = list()
        for _value in data:
            try:
                int_list.append(int(_value))
            except:
                continue
        return int_list

    @staticmethod
    def get_sanitized_float(data):
        try:
            data = float(data)
            return data
        except:
            return None

    @staticmethod
    def get_sanitized_bool(data):
        if type(data) is bool:
            return data
        try:
            return data.lower() in ("yes", "true", "t", "1")
        except:
            return None

    def get_language_slug(self):
        return self.request.GET.get('lang', settings.DEFAULT_LANGUAGE_SLUG)

    def get_request_source(self):
        request_source = self.kwargs.get('request_source', None)
        return request_source

    def get_user_permission(self, codename):
        profile = self.get_profile()
        if not profile:
            return False
        return profile.user_permissions.filter(codename=codename).exists()
