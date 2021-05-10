"""
Change the configuration file
"""
#  This file is part of FAST-OAD : A framework for rapid Overall Aircraft Design
#  Copyright (C) 2021 ONERA & ISAE-SUPAERO
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

from IPython.display import clear_output
from fastoad.change_files.change_driver import ChangeDriver
from fastoad.change_files.button import Button
from fastoad.change_files.change_name_input_output import ChangeNameInputOutput
from fastoad.change_files.change_title import ChangeTitle

class ChangeOneFile:
    """
    A class which display all the widgets for the configuration file
    """

    def _initialize_widgets(self):
        """
        Initialize widgets
        """

        ChangeTitle().display()
        ChangeNameInputOutput().display()
        ChangeDriver().display()
        Button().display()

    def display(self):
        """
        Display the user interface
        :return the display object
        """
        clear_output(wait=True)
        self._initialize_widgets()
