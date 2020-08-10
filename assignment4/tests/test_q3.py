import pathlib

from hw4.q3.hw4_q3 import *


fname = pathlib.Path('data/311_service_requests.zip').resolve()


def test_common_complaint():
    ans = common_complaint(fname)
    assert ans == ('HEATING', 73371)


def test_parking_borough():
    ans = parking_borough(fname)
    assert ans == 'BROOKLYN'
