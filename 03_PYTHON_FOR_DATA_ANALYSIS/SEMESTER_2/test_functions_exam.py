from functions_exam import analyze_text, calendar
import pytest
import pandas as pd


def test_calendar_returns_df():
    df = calendar('2025-01-01', '2025-01-02')
    assert isinstance(df, pd.DataFrame)

def test_calendar_rows():
    assert calendar('2025-01-01', '2025-01-02').shape == (48, 2) # This would work if I did the function right

def test_calendar_columns():
    df = calendar('2025-01-01', '2025-01-02')
    assert list(df.columns) == ['day', 'month', 'year', 'day_of_week', 'is_weekend', 'quarter']


def test_analyze_text_returns_df():
    df = analyze_text(["Check, check, check, is this thing on?"])
    assert isinstance(df, pd.DataFrame)

def test_analyze_text_invalid_input():
    with pytest.raises(TypeError):
        analyze_text(123)

def test_analyze_text_invalid_list():
    with pytest.raises(ValueError):
        analyze_text(['test scentence', 123, 'hello'])



if __name__ == "__main__":
    pytest.main() # This will run the tests in this file, given that you have installed pytest.