import logging
import os.path as pth

import fastoad.api as oad


class GenerateFiles:
    DATA_FOLDER_PATH = "data"

    WORK_FOLDER_PATH = "workdir"

    CONFIGURATION_FILE = pth.join(WORK_FOLDER_PATH, "oad_process.yml")
    SOURCE_FILE = pth.join(DATA_FOLDER_PATH, "CeRAS01_baseline.xml")

    # For having log messages on screen
    logging.basicConfig(level=logging.INFO, format="%(levelname)-8s: %(message)s")

    # For using all screen width
    from IPython.core.display import display, HTML

    display(HTML("<style>.container { width:95% !important; }</style>"))

    oad.generate_configuration_file(CONFIGURATION_FILE, overwrite=True)
