from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from .views import SignUp, SignUpAPIView

router = routers.DefaultRouter()
router.register('', SignUpAPIView)

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('api/auth/signup/', include(router.urls)),
    path('api/auth/login/', obtain_jwt_token),
]
