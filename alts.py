"""Alternatives shown in the detail panels."""
import json, numpy as np, pandas as pd
import blocks as B
from blocks import Q, TEAL, BLUE, AMBER, RED, VIOLET
COLORS = [TEAL, BLUE, AMBER, VIOLET, "#d6409f", "#8b8d98"]
def hav(la1, lo1, la2, lo2, R=6371.0):
    p = np.pi / 180
    a = np.sin((np.asarray(la2) - la1) * p / 2) ** 2 + np.cos(la1 * p) * np.cos(np.asarray(la2) * p) * np.sin((np.asarray(lo2) - lo1) * p / 2) ** 2
    return 2 * R * np.arcsin(np.sqrt(a))
def usd(x): return "${:,.0f}".format(x)
