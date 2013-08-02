from django.conf import settings
from .models import RequestLog

class RequestLogMiddleware(object):

    """
    Middleware that logs URL request into a database.
    """

    def process_request(self, request):
        for x in getattr(settings, 'REQUESTLOG_EXCLUDE_PATH_PREFIX', ''):
            if request.path_info.startswith(x):
                return
        log = RequestLog()
        log.ip = request.META['REMOTE_ADDR']
        log.path = request.path_info
        log.user_agent = request.META['HTTP_USER_AGENT']
        log.save()
