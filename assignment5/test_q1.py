import pathlib

import pytest

from hw5_q1 import *


def test_valid_input():
    fname = pathlib.Path('test_q1.py')
    q = QuestionnaireAnalysis(fname)
    assert fname == q.data_fname


def test_str_input():
    fname = 'test_q1.py'
    q = QuestionnaireAnalysis(fname)
    assert pathlib.Path(fname) == q.data_fname


def test_missing_file():
    fname = pathlib.Path('teststs.fdfd')
    with pytest.raises(ValueError):
        QuestionnaireAnalysis(fname)
