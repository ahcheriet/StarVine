##
# \brief Frank copula.
import numpy as np
from copula_base import CopulaBase


class FrankCopula(CopulaBase):
    """!
    @brief Frank copula.
    Single parameter
    \f$\theta \in [0, \infty) \f$
    """
    def __init__(self, rotation=0, init_params=None):
        self.thetaBounds = ((1e-9, np.inf),)
        self.theta0 = (1.0,)
        self.rotation = rotation
        self.name = 'frank'
        super(FrankCopula, self).__init__(rotation, params=init_params)

    @CopulaBase._rotPDF
    def _pdf(self, u, v, rotation=0, *theta):
        """!
        @brief Probability density function for frank bivariate copula
        """
        if theta[0] == 0:
            p = np.ones(np.array(u).size)
            return p
        else:
            h1 = -theta[0]
            h2 = expm1(h1)
            h3 = h1 * h2

            UU = np.array(u)
            VV = np.array(v)

            h4 = expm1(h1 * UU) * expm1(h1 * VV)
            p = h3 * np.exp(h1 * (UU + VV)) / np.power(h2 + h4, 2.0)
            return p

    @CopulaBase._rotCDF
    def _cdf(self, u, v, rotation=0, *theta):
        h1 = -theta[0]
        h2 = expm1(h1)

        UU = np.array(u)
        VV = np.array(v)
        h3 = expm1(h1 * UU) * expm1(h1 * VV)

        p = -np.log(1.0 + h3 / h2) / theta[0]
        return p

    @CopulaBase._rotH
    def _h(self, v, u, rotation=0, *theta):
        """
        TODO: CHECK UU and VV ordering!
        """
        h1 = np.exp(-theta[0])
        UU = np.array(u)
        VV = np.array(v)
        h2 = np.power(h1, UU)
        h3 = np.power(h1, VV)
        h4 = h2 * h3
        uu = (h4 - h3) / (h4 - h2 - h3 + h1)
        return uu

    @CopulaBase._rotHinv
    def _hinv(self, V, U, rotation=0, *theta):
        """
        TODO: CHECK UU and VV ordering!
        """
        h1 = np.exp(-theta[0])
        h2 = expm1(-theta[0])
        h3 = -1.0 / theta[0]
        UU = np.array(U)
        VV = np.array(V)
        h4 = np.power(h1, VV)

        uu = h3 * np.log(1 + h2 / (h4 * (1 / UU - 1) + 1))
        return uu

    @CopulaBase._rotGen
    def _gen(self, t, *theta):
        return -np.log((np.exp(-theta[0] * t) - 1.0) / (np.exp(-theta[0]) - 1.0))


def expm1(x):
    """!
    @brief exponential - 1.0 helper
    """
    return np.exp(x) - 1.0
