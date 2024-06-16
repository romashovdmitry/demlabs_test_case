# Django imports
from django.utils.deprecation import MiddlewareMixin


class UserToIDMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            request.user_id = request.user.id
        else:
            request.user_id = None