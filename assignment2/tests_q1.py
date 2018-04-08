"""
__author__ = Hagai Har-Gil
"""
from hw2_q1 import *


class BicycleTests:
    """
    Unit tests for the bicycle question. If no errors pop
    during the execution, and the summary printout doesn't
    contain any errors, your grade for the question will be perfect.
    """
    def test_existence(self):
        """ Asserts the class exists with the right name """
        bi = Bicycle(gear=1, cadence=20)
        print(f'Class exists:\n{bi}')
        return True

    def test_change_speed_below_0(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to(-1)
        if bi.speed < 0:
            return False
        return True

    def test_change_speed_to_non_number(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to('a')
        if 0 <= bi.speed <= 1000:
            return True
        return False

    def test_change_speed_to_higher_than_1000(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to(1300)
        if bi.speed > 1000:
            return False
        return True

    def test_cadence_remains_positive(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to(0)
        if bi.cadence < 0:
            return False
        bi.change_speed_to(1)
        if bi.cadence < 0:
            return False
        return True

    def test_gear_below_7(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to(0)
        if bi.gear < 1:
            return False
        bi.change_speed_to(1)
        if bi.gear < 1:
            return False
        return True

    def test_gear_at_high_speeds(self):
        bi = Bicycle(gear=1, cadence=20)
        bi.change_speed_to(999)
        if bi.gear > 7:
            return False
        return True

    def test_many_gear_changes(self):
        bi = Bicycle(gear=1, cadence=20)
        for speed in range(1000):
            bi.change_speed_to(speed)
        assert ((1 <= bi.gear <= 7) and (0 <= bi.speed <= 1000)), f"At a real speed of {speed},"\
                f"gear was {bi.gear} and bicycle speed was {bi.speed}."
        return True


if __name__ == '__main__':
    btests = BicycleTests()
    methods = ["existence", "change_speed_below_0", "change_speed_to_non_number",
               "change_speed_to_higher_than_1000", "cadence_remains_positive",
               "gear_below_7", "gear_at_high_speeds", "many_gear_changes"]
    results = []

    for method in methods:
        results.append(getattr(btests, "test_" + method)())

    print("--------\nSummary:")
    for res, method in zip(results, methods):
        if not res:
            print(f"Failed when testing method 'test_{method}'.")

    print("Done.")