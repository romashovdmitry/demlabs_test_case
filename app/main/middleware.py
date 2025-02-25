# JWT imports
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication


# https://docs.djangoproject.com/en/5.0/topics/http/middleware/#writing-your-own-middleware
class UserToIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """ add user_id key-valuepair to requst.data from request.user.id """
        authorization_header = request.headers.get('Authorization')
        if authorization_header:
            try:
                token_type, token = authorization_header.split()
                if token_type.lower() == 'bearer':
                    jwt_authentication = JWTTokenUserAuthentication()
                    user, validated_token = jwt_authentication.authenticate(request)
                    if user:
                        request.user_id = user.id

            except:
                # wrong header format
                return self.get_response(request)

        response = self.get_response(request)

        return response


