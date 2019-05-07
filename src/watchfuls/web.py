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

import importlib


class Watchful():
    def __init__(self):
        pass

    def check(self):
        utils = importlib.import_module('__utils')
        cmd = 'curl -sL -w "%{http_code}\n" "http://www.atareao.es/" -o /dev/null'
        stdout, stderr = utils.execute(cmd)
        if stdout.find('200') == -1:
            return False, 'www.atareao.es down'
        return True, 'www.atareao.es up'


if __name__ == '__main__':
    wf = Watchful()
    print(wf.check())