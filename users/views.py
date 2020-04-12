from django.urls import reverse_lazy
from django.views.generic import CreateView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from .forms import SignUpForm
from .models import User
from .serializers import SignUpSerializer


class SignUp(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('admin:login')
    template_name = 'signup.html'


class SignUpAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    http_method_names = ['post']
    permission_classes = (AllowAny, )
