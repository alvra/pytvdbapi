# -*- coding: utf-8 -*-

# Copyright 2011 Björn Larsson

# This file is part of pytvdbapi.
#
# pytvdbapi is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pytvdbapi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pytvdbapi.  If not, see <http://www.gnu.org/licenses/>.

"""
A module for managing banner information

Although some banners are related to a specific season, all banners will
be stored as a property of the related Show instance.
"""

from pytvdbapi import error


class Banner(object):
    """
    Representing a Banner as provided by `thetvdb.com <http://thetvdb.com>`_.

    **Attributes:**

    The number and types of attributes that the Banner has is dependent on
    the type of Banner it is. Below is a description of the different
    attributes.

    *Common*:

    These attributes are present for all Banner objects.

    * BannerPath (str). The last part of the URL pointing to the immage.\
        This is appended to the correct mirror adress to form the full URL.
    * BannerType (str). This could be any of **fanart**, **season** or \
        **poster**. This value controls what other attributes are available \
        as described below.
    * BannerType2 (str). What this attribute contains will depend on the \
        type of Banner and will be described in each sub section below.
    * Language (str).
    * Rating (float).
    * RatingCount (int).
    * id (id).
    * banner_url (str). This is generated by **pytvdbapi** and is the full \
        URL for the banner.

    *fanart:*

    Additional to the common attributes, the following attributes are included
    on objects of type **fanart**.

    * BannerType2 (str). Contains the dimension of the immage as a string.
    * Colors (list).
    * SeriesName (bool).
    * ThumbnailPath (str).
    * VignettePath (str).

    *poster:*

    **poster** type does not contain any additional attributes.

    * BannerType2 (str). Contains the dimension of the immage as a string.

    *season:*

    Additional to the common attributes, the following attributes are included
    on objects of type **season**.

    * BannerType2 (str). Contains the word 'season'
    * Season (int).

    Example::

        >>> from pytvdbapi import api
        >>> db = api.TVDB('B43FF87DE395DF56', banners=True)
        >>> show = db.get( 79349, "en" )  # Dexter
        >>> show.update()
        >>> assert len(show.banner_objects) > 0
        >>> banner = show.banner_objects[0]
        >>> banner.banner_url
        'http://thetvdb.com/banners/fanart/original/79349-42.jpg'
        >>> banner.Language
        'en'

    Showing the different banner types and their attributes.

        >>> fanart = [b for b in show.banner_objects \
if b.BannerType == "fanart"]
        >>> dir(fanart[0]) #doctest: +NORMALIZE_WHITESPACE
        ['BannerPath', 'BannerType', 'BannerType2', 'Colors', 'Language',
        'Rating', 'RatingCount', 'SeriesName', 'ThumbnailPath', 'VignettePath',
        'banner_url', 'id']
        >>> fanart[0].BannerType2
        '1920x1080'

        >>> posters = [b for b in show.banner_objects \
if b.BannerType == "poster"]
        >>> dir(posters[0]) #doctest: +NORMALIZE_WHITESPACE
        ['BannerPath', 'BannerType', 'BannerType2', 'Language', 'Rating',
        'RatingCount', 'banner_url', 'id']
        >>> posters[0].BannerType2
        '680x1000'

        >>> seasons = [b for b in show.banner_objects \
if b.BannerType == "season"]
        >>> dir(seasons[0]) #doctest: +NORMALIZE_WHITESPACE
        ['BannerPath', 'BannerType', 'BannerType2', 'Language', 'Rating',
        'RatingCount', 'Season', 'banner_url', 'id']
        >>> seasons[0].BannerType2
        'season'

    """
    def __init__(self, mirror, data, show):
        self.mirror, self.data, self.show = mirror, data, show

    def __repr__(self):
        return "<Banner>"

    def __getattr__(self, item):
        if item == "banner_url":
            return self.mirror + "/banners/" + self.BannerPath
        else:
            try:
                return self.data[item]
            except KeyError:
                raise error.TVDBAttributeError(
                    "Banner has no {0} attribute".format(item))

    def __dir__(self):
        return list(self.data.keys()) + ["banner_url"]
