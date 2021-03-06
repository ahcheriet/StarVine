##
# \brief Test copula rotations
from __future__ import print_function, division
from pc_base import PairCopula
from copula_factory import Copula
import unittest
import numpy as np
import seaborn as sns
from scipy.stats import kendalltau
from six import iteritems
import os
pwd_ = os.getcwd()
dataDir = pwd_ + "/tests/data/"
np.random.seed(123)


class TestRotateCopula(unittest.TestCase):
    def testGumbelRotate(self):
        expectedKtaus = {0: 0.87499, 1: -0.87499, 2: 0.87499, 3: -0.87499}
        shapeParam = 8.0
        for rotation, expectedKtau in iteritems(expectedKtaus):
            gumbel = Copula("gumbel", rotation)
            u, v = gumbel.sample(10000, *(shapeParam,))
            g = sns.jointplot(u, v, stat_func=kendalltau)
            g.savefig("gumbel_sample_pdf_" + str(rotation) + ".png")
            gumbel.fittedParams = (shapeParam,)
            c_kTau = gumbel.kTau()
            # check kTau
            self.assertAlmostEqual(c_kTau, expectedKtau, delta=0.001)
            # compute rank corr coeff from resampled data
            gumbel_model = PairCopula(u, v)
            gumbel_model.copulaTournament()
            print(gumbel_model.copulaParams)
            self.assertTrue("gumbel" in gumbel_model.copulaModel.name)
            # Ensure fitted shape parameter is same as original
            self.assertAlmostEqual(shapeParam, gumbel_model.copulaParams[1][0], delta=0.2)
            self.assertEqual(rotation, gumbel_model.copulaParams[3])
            # Ensure kTau is nearly the same from resampled data
            self.assertAlmostEqual(c_kTau, gumbel_model.copulaModel.kTau(), delta=0.02)
            # fit to resampled data
            u_model, v_model = gumbel_model.copulaModel.sample(10000)
            gumbel_refit = PairCopula(u_model, v_model)
            gumbel_refit.copulaTournament()
            u_resample, v_resample = gumbel_refit.copulaModel.sample(1000)
            self.assertAlmostEqual(c_kTau, gumbel_refit.copulaModel.kTau(), delta=0.05)
            # plot resampled data
            g_resample = sns.jointplot(u_resample, v_resample, stat_func=kendalltau)
            g_resample.savefig("gumbel_resample_pdf_" + str(rotation) + ".png")

    def testFrankRotate(self):
        expectedKtaus = {0: 0.602619667, 1: -0.602619667, 2: 0.602619667, 3: -0.602619667}
        shapeParam = 8.0
        for rotation, expectedKtau in iteritems(expectedKtaus):
            frank = Copula("frank", rotation)
            u, v = frank.sample(10000, *(shapeParam,))
            g = sns.jointplot(u, v, stat_func=kendalltau)
            g.savefig("frank_sample_pdf_" + str(rotation) + ".png")
            frank.fittedParams = (shapeParam,)
            c_kTau = frank.kTau()
            # check kTau
            self.assertAlmostEqual(c_kTau, expectedKtau, delta=0.001)
            # compute rank corr coeff from resampled data
            frank_model = PairCopula(u, v)
            frank_model.copulaTournament()
            print(frank_model.copulaParams)
            self.assertTrue("frank" in frank_model.copulaModel.name)
            # Ensure refitted shape parameter is same as original
            self.assertAlmostEqual(shapeParam, frank_model.copulaParams[1][0], delta=0.2)
            # Ensure kTau is nearly the same from resampled data
            self.assertAlmostEqual(c_kTau, frank_model.copulaModel.kTau(), delta=0.02)
            # fit to resampled data
            u_model, v_model = frank_model.copulaModel.sample(10000)
            frank_refit = PairCopula(u_model, v_model)
            frank_refit.copulaTournament()
            u_resample, v_resample = frank_refit.copulaModel.sample(1000)
            self.assertAlmostEqual(c_kTau, frank_refit.copulaModel.kTau(), delta=0.05)
            # plot resampled data
            g_resample = sns.jointplot(u_resample, v_resample, stat_func=kendalltau)
            g_resample.savefig("frank_resample_pdf_" + str(rotation) + ".png")

    def testClaytonRotate(self):
        expectedKtaus = {0: 0.7777777, 1: -0.7777777, 2: 0.7777777, 3: -0.7777777}
        shapeParam = 7.0
        for rotation, expectedKtau in iteritems(expectedKtaus):
            clayton = Copula("clayton", rotation)
            u, v = clayton.sample(10000, *(shapeParam,))
            g = sns.jointplot(u, v, stat_func=kendalltau)
            g.savefig("clayton_sample_pdf_" + str(rotation) + ".png")
            clayton.fittedParams = (shapeParam,)
            c_kTau = clayton.kTau()
            # check kTau
            self.assertAlmostEqual(c_kTau, expectedKtau, delta=0.001)
            # compute rank corr coeff from resampled data
            clayton_model = PairCopula(u, v)
            clayton_model.copulaTournament()
            print(clayton_model.copulaParams)
            self.assertTrue("clayton" in clayton_model.copulaModel.name)
            # Ensure fitted shape parameter is same as original
            self.assertAlmostEqual(shapeParam, clayton_model.copulaParams[1][0], delta=0.2)
            self.assertEqual(rotation, clayton_model.copulaParams[3])
            # Ensure kTau is nearly the same from resampled data
            self.assertAlmostEqual(c_kTau, clayton_model.copulaModel.kTau(), delta=0.02)
            # fit to resampled data
            u_model, v_model = clayton_model.copulaModel.sample(10000)
            clayton_refit = PairCopula(u_model, v_model)
            clayton_refit.copulaTournament()
            u_resample, v_resample = clayton_refit.copulaModel.sample(1000)
            self.assertAlmostEqual(c_kTau, clayton_refit.copulaModel.kTau(), delta=0.05)
            # plot resampled data
            g_resample = sns.jointplot(u_resample, v_resample, stat_func=kendalltau)
            g_resample.savefig("clayton_resample_pdf_" + str(rotation) + ".png")

    def testGaussRotate(self):
        shapes = {0: 0.7777777, 1: -0.7777777, 2: 0.7777777, 3: -0.7777777}
        for rotation, shapeParam in iteritems(shapes):
            gauss = Copula("gauss", 0)
            u, v = gauss.sample(10000, *(shapeParam,))
            g = sns.jointplot(u, v, stat_func=kendalltau)
            g.savefig("gauss_sample_pdf_" + str(rotation) + ".png")
            gauss.fittedParams = (shapeParam,)
            c_kTau = gauss.kTau()
            # compute rank corr coeff from resampled data
            gauss_model = PairCopula(u, v)
            gauss_model.copulaTournament()
            print(gauss_model.copulaParams)
            self.assertTrue("gauss" in gauss_model.copulaModel.name)
            # Ensure fitted shape parameter is same as original
            self.assertAlmostEqual(shapeParam, gauss_model.copulaParams[1][0], delta=0.2)
            # Ensure kTau is nearly the same from resampled data
            self.assertAlmostEqual(c_kTau, gauss_model.copulaModel.kTau(), delta=0.02)
            # fit to resampled data
            u_model, v_model = gauss_model.copulaModel.sample(10000)
            gauss_refit = PairCopula(u_model, v_model)
            gauss_refit.copulaTournament()
            u_resample, v_resample = gauss_refit.copulaModel.sample(1000)
            self.assertAlmostEqual(c_kTau, gauss_refit.copulaModel.kTau(), delta=0.05)
            self.assertAlmostEqual(shapeParam, gauss_refit.copulaParams[1][0], delta=0.2)
            # plot resampled data
            g_resample = sns.jointplot(u_resample, v_resample, stat_func=kendalltau)
            g_resample.savefig("gauss_resample_pdf_" + str(rotation) + ".png")
