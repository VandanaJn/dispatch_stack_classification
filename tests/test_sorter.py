import pytest
from src.sorter import is_bulky, is_heavy, sort, VOL_THRESHOLD, DIM_THRSHOLD, MASS_THRSHOLD, STACK_REJECTED, STACK_SPECIAL, STACK_STANDARD


class TestIsBulky:
    @pytest.mark.parametrize("width,height,length,expected", [
        # Volume >= 1,000,000
        (100, 100, 100, True),  # 1,000,000 exactly
        (101, 100, 100, True),  # > 1,000,000
        # Any dimension >= 150
        (150, 10, 10, True),
        (10, 150, 10, True),
        (10, 10, 150, True),
        (160, 10, 10, True),
        # Neither
        (10, 10, 10, False),
        (149, 10, 10, False),
        (10, 149, 10, False),
        (10, 10, 149, False),
        (99, 100, 100, False),  # volume < 1,000,000
    ])
    def test_is_bulky(self, width, height, length, expected):
        assert is_bulky(width, height, length) == expected


class TestIsHeavy:
    @pytest.mark.parametrize("mass,expected", [
        (20, True),   # exactly 20
        (21, True),   # > 20
        (19.9, False), # < 20
        (0, False),
        (10, False),
    ])
    def test_is_heavy(self, mass, expected):
        assert is_heavy(mass) == expected


class TestSort:
    @pytest.mark.parametrize("width,height,length,mass,expected", [
        # Both bulky and heavy -> REJECTED
        (150, 150, 150, 20, STACK_REJECTED),  # bulky by dimension, heavy
        (100, 100, 100, 20, STACK_REJECTED),  # bulky by volume, heavy
        # Bulky but not heavy -> SPECIAL
        (150, 10, 10, 10, STACK_SPECIAL),  # bulky by dimension, not heavy
        (100, 100, 100, 10, STACK_SPECIAL),  # bulky by volume, not heavy
        # Heavy but not bulky -> SPECIAL
        (10, 10, 10, 20, STACK_SPECIAL),  # not bulky, heavy
        (10, 10, 10, 25, STACK_SPECIAL),
        # Neither -> STANDARD
        (10, 10, 10, 10, STACK_STANDARD),
        (149, 10, 10, 19.9, STACK_STANDARD),
        (99, 100, 100, 19.9, STACK_STANDARD),  # volume < 1M, mass < 20
    ])
    def test_sort(self, width, height, length, mass, expected):
        assert sort(width, height, length, mass) == expected