#!/usr/bin/python2
from __future__ import print_function, division
# starvine imports
import context
from starvine.vine.C_vine import Cvine
from starvine.mvar.mv_plot import matrixPairPlot
# extra imports
import unittest
import os
import numpy as np
import pandas as pd
pwd_ = os.path.dirname(os.path.abspath(__file__))
dataDir = pwd_ + "/data/"
np.random.seed(123)


class TestCvine(unittest.TestCase):
    def testCvineConstruct(self):
        stocks = np.loadtxt(dataDir + 'stocks.csv', delimiter=',')
        x = stocks[:, 0]
        y = stocks[:, 1]
        z = stocks[:, 4]
        # Create pandas data table
        tstData = pd.DataFrame()
        tstData[0] = x
        tstData[1] = y
        tstData[2] = z
        # Visualize multivar data
        matrixPairPlot(tstData, savefig="tri_varaite_ex.png")

        # Init Cvine
        tstVine = Cvine(tstData)

        # construct the vine
        tstVine.constructVine()

        # plot vine
        tstVine.plotVine(savefig="c_vine_graph_ex.png")


if __name__ == "__main__":
    unittest.main()