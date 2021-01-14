"""
Output Parameter Controller

@author:    David Schote
@reworked by: Sula Mueller
@contact:   david.schote@ovgu.de
@version:   2.0.2
@change:    02/11/2020

@summary:   Class to write output values on the UI
"""

from PyQt5.QtCore import QObject
from PyQt5.uic import loadUiType

Parameter_Form, Parameter_Base = loadUiType('view/outputparameter.ui')

# Output Parameter Widget-Class
class OutputParameter(Parameter_Base, Parameter_Form):

    def __init__(self, name, value):
        super(OutputParameter, self).__init__()
        self.setupUi(self)

        # Set output parameter's label and value
        self.label_name.setText(name)
        self.output_value.setText(str(value))

    def set_value(self, value: int) -> None:
        self.output_value.setText(str(value))

class Output(QObject):
    def __init__(self, parent=None):
        super(Output, self).__init__(parent)

        # Make parent reachable from outside __init__
        self.parent = parent

    def set_parameters(self, values: dict):
        # Reset grid layout for output parameter
        for i in reversed(range(self.parent.layout_outputgrid.count())):
            self.parent.layout_outputgrid.itemAt(i).widget().setParent(None)
        # Add values as output parameters to grid layout
        row = 0
        col = 0
        for parameter in list(values.keys()):
            if row > 2:
                col += 1
                row = 0
            item = OutputParameter(parameter, values[parameter])
            self.parent.layout_outputgrid.addWidget(item, row, col)
            row += 1