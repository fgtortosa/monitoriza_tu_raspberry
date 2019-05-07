#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# Monitorize your Raspberry Pi
#
# Copyright © 2019  Lorenzo Carbonell (aka atareao)
# <lorenzo.carbonell.cerezo at gmail dot com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import codecs
import json

class Config(object):
    def __init__(self, file):
        self.file = file

    def read(self):
        data = {}
        try:
            f = codecs.open(self.file, 'r', 'utf-8')
            data = json.loads(f.read())
            f.close()
        except Exception as e:
            print(e)
        return data

    def save(self, data):
        f = codecs.open(self.file, 'w', 'utf-8')
        f.write(json.dumps(data))
        f.close()
