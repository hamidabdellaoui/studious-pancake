import pytest
from datetime import date
from financial_library import Curve



@pytest.fixture
def curve():
    curve = Curve()
    curve.add_instrument(1, 0.01)
    curve.add_instrument(2, 0.015)
    curve.add_instrument(3, 0.02)
    return curve


def test_add_instrument(curve):
    assert len(curve.instruments) == 3
    assert curve.instruments[0]["term"] == 1
    assert curve.instruments[0]["rate"] == 0.01


def test_remove_instrument(curve):
    curve.remove_instrument(2)
    assert len(curve.instruments) == 2
    assert curve.instruments[1]["term"] == 3
    assert curve.instruments[1]["rate"] == 0.02


def test_discount_factor(curve):
    assert round(curve.discount_factor(2), 6) == 0.985222


def test_interpolate(curve):
    assert round(curve.interpolate(1.5), 6) == 0.0125


def test_plot_curve(curve):
    curve.plot_curve()
