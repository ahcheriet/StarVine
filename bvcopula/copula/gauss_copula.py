##
# \brief Gaussian copula (special case of t-copula where DoF = \inf)
import numpy as np
import scipy as sp
from scipy.special import gamma
from copula_base import CopulaBase


class GaussCopula(CopulaBase):
    def __init__(self):
        pass

    def _pdf(self, u, v, rotation=0, *theta):
        """!
        @brief Probability density function of T copula.
        @param u <np_1darary>
        @param v <np_1darary>
        @param rotation <int>  Optional copula rotation.
        @param theta <list of float> list of parameters to T-copula
            [Shape, DoF]
        """
        # Constants
        rho2 = np.power(theta[0], 2.0)
        h1 = 1-rho2
        h2 = rho2 / (2.0 * h1)
        h3 = theta / h1

        # T random var with theta[1] DoF parameter (unit SD, centered at 0)
        norm_rv = sp.stats.norm(scale=1.0, loc=0.0)

        # Output storage
        p = np.zeros(len(u))

        # UU = CheckBounds(u);
        # VV = CheckBounds(v);
        # u and v must be on the unit square ie. in [0, 1]
        UU = np.array(u)  # TODO: check bounds
        VV = np.array(v)

        # quantile function is the inverse CDF
        x = norm_rv.ppf(UU)
        y = norm_rv.ppf(VV)

        p = np.exp(h3 * x  * y - h2 * (np.power(x, 2) + np.power(y, 2))) / np.sqrt(h1)
        return p


    def _h(self, u, v, rotation=0, *theta):
        """!
        @brief H function (Conditional distribution) of T copula.
        """
        h1 = np.sqrt(1.0 - np.power(np.array(theta), 2))
        dist = sp.stats.norm(scale=1.0, loc=0.0)

        UU = np.array(u)  # TODO: check input bounds
        VV = np.array(v)

        # inverse CDF yields quantiles
        x = dist.ppf(UU)
        y = dist.ppf(VV)

        # eval H function
        uu = dist.cdf((x - theta[0] * y) / h1)
        return uu


    def _hinv(self, u, v, rotation=0, *theta):
        """!
        @brief Inverse H function (Inv Conditional distribution) of T copula.
        """
        h1 = np.sqrt(1.0 - np.power(np.array(theta), 2))
        dist = sp.stats.norm(scale=1.0, loc=0.0)

        UU = np.array(u)  # TODO: check input bounds
        VV = np.array(v)

        # inverse CDF yields quantiles
        x = dist.ppf(UU)
        y = dist.ppf(VV)

        # eval H function
        uu = dist.cdf(x * h1 + theta * y)
        return uu