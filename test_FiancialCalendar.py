import pytest
from datetime import date, timedelta
from my_library import FinancialCalendar

@pytest.fixture
def cal():
    return FinancialCalendar()

def test_is_business_day(cal):
    assert cal.is_business_day(date(2022, 1, 1)) == False
    assert cal.is_business_day(date(2022, 1, 3)) == False
    assert cal.is_business_day(date(2022, 1, 4)) == True

def test_add_business_day(cal):
    assert cal.add_business_day(date(2022, 1, 1), 1) == date(2022, 1, 4)
    assert cal.add_business_day(date(2022, 1, 4), -1) == date(2022, 1, 3)
    assert cal.add_business_day(date(2022, 1, 4), 0) == date(2022, 1, 4)
