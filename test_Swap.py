import pytest
from datetime import date
from library import Swap, FinancialCalendar, Curve

def test_swap_price():
    # Set up a financial calendar
    holidays = [date(2022, 1, 1), date(2022, 12, 25)]
    cal = FinancialCalendar(holidays)
    
    # Set up a curve with some instruments
    curve = Curve()
    curve.add_instrument(0.25, 0.01)
    curve.add_instrument(0.5, 0.015)
    curve.add_instrument(1.0, 0.02)
    curve.add_instrument(2.0, 0.025)
    curve.add_instrument(5.0, 0.03)
    
    # Set up a swap
    start_date = date(2022, 1, 1)
    maturity_date = date(2022, 7, 1)
    notional = 1000000
    fixed_rate = 0.02
    freq = 2
    
    swap = Swap(start_date, maturity_date, notional, fixed_rate, freq, cal)
    
    # Test the present value calculation
    pv = swap.calculate_present_value(curve)
    
    # Expected present value calculated using QuantLib
    # (assuming a flat yield curve at 2%)
    expected_pv = 9832.22
    
    assert abs(pv - expected_pv) < 0.01
