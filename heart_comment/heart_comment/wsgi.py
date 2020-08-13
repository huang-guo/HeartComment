"""
WSGI config for heart_comment project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

profile = os.environ.get('COMMENT_PROFILE','develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'heart_comment.settings.%s' % profile)

application = get_wsgi_application()
