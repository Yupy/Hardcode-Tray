#!/usr/bin/python3
"""
Fixes Hardcoded tray icons in Linux.

Author : Bilal Elmoussaoui (bil.elmoussaoui@gmail.com)
Contributors : Andreas Angerer, Joshua Fogg
Version : 3.6.2
Website : https://github.com/bil-elmoussaoui/Hardcode-Tray
Licence : The script is released under GPL, uses a modified script
     form Chromium project released under BSD license
This file is part of Hardcode-Tray.
Hardcode-Tray is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Hardcode-Tray is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with Hardcode-Tray. If not, see <http://www.gnu.org/licenses/>.
"""
from os import remove, path
from modules.utils import copy_file, replace_colors


class SVG:
    """SVG Interface used by other class's."""

    _is_svg_enabled = True

    def __init__(self, colors):
        """Init function."""
        self.colors = colors

    def to_png(self, input_file, output_file, width=None, height=None):
        """Convert svg to png and save it in a destination."""
        width, height = self.get_size(width, height)
        tmp_file = ""
        if len(self.colors) != 0:
            tmp_file = "/tmp/{0!s}".format(path.basename(input_file))
            copy_file(input_file, tmp_file)
            input_file = tmp_file
            replace_colors(input_file, self.colors)
        self.convert_to_png(input_file, output_file, width, height)
        if tmp_file and path.isfile(tmp_file):
            remove(tmp_file)

    def to_bin(self, input_file, width=None, height=None):
        """Convert svg to binary."""
        self.to_png(input_file, self.outfile, width, height)
        with open(self.outfile, 'rb') as temppng:
            binary = temppng.read()
        temppng.close()
        remove(self.outfile)
        return binary

    def is_installed(self):
        """Check if the tool is installed."""
        pass

    def get_size(self, width, height):
        """Return the size of the icon."""
        if width and not height:
            width = height
        elif height and not width:
            height = width
        return width, height

    @property
    def is_svg_enabled(self):
        """Return if the svg to png conversion tools are activated."""
        return self._is_svg_enabled

    @is_svg_enabled.setter
    def is_svg_enabled(self, is_svg_enabled):
        """Disable using svg to png conversion tools."""
        self._is_svg_enabled = is_svg_enabled
