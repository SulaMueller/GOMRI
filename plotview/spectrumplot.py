"""
Plotview Spectrum (1D Plot)

@author:    David Schote, Sula Mueller
@contact:   david.schote@ovgu.de
@version:   2.0 (Beta)
@change:    13/12/2020

@summary:   Class for plotting a spectrum

@status:    Plots x and y data

"""

from pyqtgraph import GraphicsLayoutWidget, PlotItem
from warnings import warn


class SpectrumPlot (GraphicsLayoutWidget):
    def __init__(self,
                 xData: list,
                 yData: list,
                 xLabel: str,
                 yLabel: str
                 ):
        super(SpectrumPlot, self).__init__()

        if len(xData) != len(yData):
            warn("Length of x and y data does not match.")
            return

        self.plotitem = self.addPlot(row=0, col=0)
        self.plotitem.plot(xData, yData, pen=(1,2))

        print("Plotting x = {}, y = {}".format(xLabel, yLabel))
    
    def addData(self, x, y):
        self.plotitem.plot(x, y, symbol='o', pen=(2,2))
        


