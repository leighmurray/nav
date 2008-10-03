# -*- coding: utf-8 -*-
#
# Copyright 2007-2008 UNINETT AS
#
# This file is part of Network Administration Visualized (NAV)
#
# NAV is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# NAV is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NAV; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Authors: Stein Magnus Jodal <stein.magnus.jodal@uninett.no>
#

"""Main Django URL configuration"""

__copyright__ = "Copyright 2007-2008 UNINETT AS"
__license__ = "GPL"
__author__ = "Stein Magnus Jodal (stein.magnus.jodal@uninett.no)"

# Import all submodules in the urls package
import os
__all__ = []
for file_name in os.listdir(os.path.dirname(__file__)):
    if file_name.endswith('.py') and not file_name.startswith('__init__'):
        module_name = file_name.replace('.py', '')
        __all__.append(module_name)
from nav.django.urls import *

# Combine urlpatterns from all the submodules
from django.conf.urls.defaults import *
urlpatterns = patterns('')
for module_name in __all__:
    urlpatterns += eval(module_name + '.get_urlpatterns()')

