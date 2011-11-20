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

__all__ = ['merge']

def merge(d1, d2, decision = lambda x,y:y):
    """
    Merging two dictionaries together using *decision* to determine what
    values will be used.
    """

    result = dict(d1)
    for k,v in d2.iteritems():
        if k in result:
            result[k] = decision(result[k], v)
        else:
            result[k] = v
    return result