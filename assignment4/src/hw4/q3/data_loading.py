import pathlib

import pandas as pd


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
    return pd.read_csv(fname, header=0, index_col=0)

