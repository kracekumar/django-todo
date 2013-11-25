# -*- coding: utf-8 -*-

from django.template import RequestContext

from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt

from todo.models import User


# Create your views here.
class ProfileView(View):
    template_name = "profile.html"
    model = User

    def get(self):
        pass


@csrf_exempt
def auth_success(request, *args, **kwargs):
    raise
    pass