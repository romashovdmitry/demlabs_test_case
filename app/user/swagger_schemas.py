# Swagger imports
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
    OpenApiExample,
    OpenApiResponse
)
from drf_spectacular.types import OpenApiTypes



swagger_schema_create_user = extend_schema(
        tags=["User"],
        summary="Create new user",
        description='POST request to create new user',
        auth=None,
        operation_id="Create new user",
        examples=[
            OpenApiExample(
                'Example: succes created user',
                value={
                    "email": "club_admin@mail.com",
                    "password": "123njkQ6**N1q",
                }
            ),
        ],
        # NOTE: можно добавить больше в responses, если будет время
        responses={
            201: None,
        }
    )


swagger_schema_login_user = extend_schema(
        tags=["User"],
        summary="Login existing user",
        description='POST request to Login existing user',
        auth=None,
        operation_id="Login existing user",
        examples=[
            OpenApiExample(
                'Example: succes login user',
                value={
                    "email": "club_admin@mail.com",
                    "password": "123njkQ6**N1q"
                }
            ),
        ],
        responses={
            200: None,
        }
    )