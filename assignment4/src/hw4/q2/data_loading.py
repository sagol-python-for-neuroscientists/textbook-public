import pathlib

import pandas as pd
import numpy as np


def load_data(fname: pathlib.Path) -> pd.DataFrame:
    """Loads the given table to memory.

    Parameters
    ----------
    fname : pathlib.path
        Filename to read as a DataFrame

    Returns
    -------
    pd.DataFrame
    """
    return pd.read_csv(fname, index_col=0, sep="\t", dtype=np.int64)
