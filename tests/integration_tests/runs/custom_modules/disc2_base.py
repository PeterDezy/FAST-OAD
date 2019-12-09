"""
    Sellar discipline 2
"""
#  This file is part of FAST : A framework for rapid Overall Aircraft Design
#  Copyright (C) 2019  ONERA/ISAE
#  FAST is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

from openmdao.api import ExplicitComponent


class Disc2Base(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate Disc2 discipline """

    def setup(self):
        self.add_input('category1:z', val=[5, 2], desc='')  # for testing non-None units
        self.add_input('y_vars:y1', val=1.0, desc='')

        self.add_output('y_vars:y2', val=1.0, desc='')
        self.declare_partials('*', '*', method='fd')
