# -*- coding: utf-8 -*-

# Copyright 2011 Björn Larsson

# This file is part of thetvdb.
#
# thetvdb is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# thetvdb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with thetvdb.  If not, see <http://www.gnu.org/licenses/>.

"""
"""

import os
import httplib2
from thetvdb import error, get_logger


#Module logger object
logger = get_logger(__name__)

class Loader(object):
    def __init__(self, cache_path):
        self.http = httplib2.Http( cache = os.path.abspath( cache_path ) )

    def load(self, url, cache=True):
        """
        :param url: The URL to be loaded
        :param cache: Optional. Set if the cache should be ignored or not.
        :return: The content of the url as bytes
        :raise: ConnectionError if the url could not be loaded

        
        """

        logger.debug("Loading data from {0}".format(url))
        
        header = dict()
        if not cache:
            logger.debug("Ignoring cached data.")
            header['cache-control'] = 'no-cache'

        try:
            response, content = self.http.request( url, headers= header )
        except ( httplib2.RelativeURIError, httplib2.ServerNotFoundError ):
            raise error.ConnectionError(
                "Unable to connect to {0}".format(url))
        else:
            return content
