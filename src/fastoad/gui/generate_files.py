"""
Defines the analysis and plotting functions for postprocessing regarding the mission
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

import os.path as pth
import openmdao.api as om
import logging
import shutil
import fastoad.api as oad


class GenerateFiles:
    DATA_FOLDER_PATH = 'data'

    WORK_FOLDER_PATH = '../notebooks/workdir'

    CONFIGURATION_FILE = pth.join(WORK_FOLDER_PATH, 'oad_process.yml')
    SOURCE_FILE = pth.join(DATA_FOLDER_PATH, 'CeRAS01_baseline.xml')

    # For having log messages on screen
    logging.basicConfig(level=logging.INFO, format='%(levelname)-8s: %(message)s')

    # For using all screen width
    from IPython.core.display import display, HTML
    display(HTML("<style>.container { width:95% !important; }</style>"))

    oad.generate_configuration_file(CONFIGURATION_FILE, overwrite=True)
