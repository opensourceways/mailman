# -*- coding: utf-8 -*-
# Copyright (C) 1998-2017 by the Free Software Foundation, Inc.
#
# This file is part of HyperKitty.
#
# HyperKitty is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# HyperKitty is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# HyperKitty.  If not, see <http://www.gnu.org/licenses/>.

"""
This file is the main URL config for a Django website including HyperKitty.
"""

from django.conf import settings
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, reverse_lazy
from django.views.generic import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(
        url=reverse_lazy('hk_root'))),
    path('hyperkitty/', include('hyperkitty.urls')),
    # url(r'^postorius/', include('postorius.urls')),
    path('', include('django_mailman3.urls')),
    path('accounts/', include('allauth.urls')),
    # Django admin
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
