# DRF imports
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http.response import HttpResponse


@api_view(http_method_names=['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """ just to check is server working or not """
    return HttpResponse(status=200)
