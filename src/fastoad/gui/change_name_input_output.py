import yaml
from IPython.display import display
from IPython.display import clear_output
import ipywidgets as widgets
from ruamel.yaml import YAML


class ChangeNameInputOutput:
    """
    Change the name of the input/output files
    """
    def __init__(self):
        # The file name
        self.file_name = "../notebooks/workdir/oad_process.yml"

        self.inputf = None

        self.outputf = None

    def save(self):
        clear_output(wait=True)
        display(self.i, self.o, self.button)

        with open(self.file_name) as f:
            content = yaml.load(f)

            self.inputf = content["input_file"]
            self.outputf = content["output_file"]

            self.inputf = self.inputf[2:len(self.inputf) - 4]

            self.outputf = self.outputf[2:len(self.outputf) - 4]
        try:
            content['input_file'] = "./" + self.i.value + ".xml"
            content['output_file'] = "./" + self.o.value + ".xml"
            with open(self.file_name, 'w') as f:
                yaml.dump(content, f)
                if self.inputf == self.i.value and self.outputf == self.o.value:
                    print("Valeurs inchangées.\n")
                else:
                    print("Successfuly changed values !\n")
                    print("Your new values :\n")
                    print("./" + self.i.value + ".xml")
                    print("./" + self.o.value + ".xml\n")
        except:
            raise ValueError("Error while modifying.\n")

    def read(self):
        yaml = YAML()

        with open(self.file_name) as f:
            content = yaml.load(f)

        self.inputf = self.content["input_file"]
        self.outputf = self.content["output_file"]

        self.inputf = self.inputf[2:len(self.inputf) - 4]

        self.outputf = self.outputf[2:len(self.outputf) - 4]

    def createwidgets(self):
        i = widgets.Text(
            value=self.inputf,
            description='input_file:',
        )

        o = widgets.Text(
            value=self.outputf,
            description='output_file:',
        )

        button = widgets.Button(
            description='Save',
            icon='save'
        )

        def on_save_button_clicked(b):
            self.save()

        button.on_click(on_save_button_clicked)

    def display(self) -> display:
        return display(self.i, self.o, self.button)
