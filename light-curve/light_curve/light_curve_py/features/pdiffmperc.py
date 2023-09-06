from dataclasses import dataclass

import numpy as np
from scipy.stats.mstats import mquantiles

from ._base import BaseSingleBandFeature
from ..dataclass_field import dataclass_field


@dataclass()
class PercentDifferenceMagnitudePercentile(BaseSingleBandFeature):
    quantile: float = dataclass_field(default=0.25, kw_only=True)

    def _eval_single_band(self, t, m, sigma=None):
        median = np.median(m)
        q1, q2 = mquantiles(m, [self.quantile, 1 - self.quantile], alphap=0.5, betap=0.5)
        return (q2 - q1) / median

    @property
    def size_single_band(self):
        return 1


__all__ = ("PercentDifferenceMagnitudePercentile",)
