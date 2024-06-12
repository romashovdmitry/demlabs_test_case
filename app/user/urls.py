# Django imports
from django.urls import path

# custom DRF classes imports
from user.views import UserCreateUpdate

# JWT imports
from rest_framework_simplejwt.views import TokenRefreshView

user_actions = UserCreateUpdate.as_view({"post": "create_user"})
login_user = UserCreateUpdate.as_view({"post": "login_user"})

urlpatterns = [
    path('', user_actions, name="user_actions"),
    path('login_user/', login_user, name="login_user"),
    # JWT
    path('refresh_token/', TokenRefreshView.as_view(), name="refresh_token"),
]