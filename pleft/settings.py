# -*- coding: utf-8 -*-

# Copyright 2010 Sander Dijkhuis <sander.dijkhuis@gmail.com>
#
# This file is part of Pleft.
#
# Pleft is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pleft is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Pleft. If not, see <http://www.gnu.org/licenses/>.

# Django settings for Pleft.

import os

from plapp.settings_common import *
from local_settings import *

TEMPLATE_DEBUG = DEBUG

SITE_NAME = 'Upstream University'

ALPHA = False

ADMINS = (
    ('Adolfo Brandes', 'arbrandes@upstream-university.org'),
)

MANAGERS = ADMINS

SITE_BASE = 'http://' +  SITE_DOMAIN

STATIC_URL = '/static/'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

LANGUAGE_CODE = 'en'
USE_I18N = True

LANGUAGES = (
    ('en', 'English'),
    ('fr', 'Français'),
    ('de', 'Deutsch'),
    ('es_ES', 'Español'),
    ('it', 'Italiano'),
    ('nl', 'Nederlands'),
    ('ru', 'Русский'),
)

ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIRS = (
    ROOT_PATH + '/templates',
)

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

ABUSE_EMAIL = 'abuse@upstream-university.org'
MAIL_SENDER = 'Upstream University <noreply@upstream-university.org>'

EMAIL_LOGO = SITE_BASE + '/static/site/images/mail-logo.png'
EMAIL_INFO = 'info@upstream-university.org'

SCREENSHOT = SITE_BASE + '/static/images/thumbnail.png'
