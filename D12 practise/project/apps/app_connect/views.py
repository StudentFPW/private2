from django.views.generic import ListView

from apps.app_connect.models import User

import logging  # Import logging module for LOGGING array

logger = logging.getLogger(__name__)  # Take name of file


class SimpleView(ListView):
    model = User
    template_name = 'user.html'
    context_object_name = 'user'
