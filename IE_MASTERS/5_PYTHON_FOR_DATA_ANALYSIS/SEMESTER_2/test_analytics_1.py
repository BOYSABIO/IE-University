import pytest
import numpy as np
from analytics_1 import stats_report, divide

def test_stats_report_with_positive_numbers():
    data = [1, 2, 3, 4, 5]
    expected_output = {
        'mean': np.mean(data),
        'median': np.median(data),
        'std': np.std(data)
    }
    assert stats_report(data) == expected_output

def test_stats_report_with_negative_numbers():
    data = [-1, -2, -3, -4, -5]
    expected_output = {
        'mean': np.mean(data),
        'median': np.median(data),
        'std': np.std(data)
    }
    assert stats_report(data) == expected_output

def test_stats_report_with_mixed_numbers():
    data = [1, -1, 2, -2, 3, -3]
    expected_output = {
        'mean': np.mean(data),
        'median': np.median(data),
        'std': np.std(data)
    }
    assert stats_report(data) == expected_output

def test_stats_report_with_single_value():
    data = [5]
    expected_output = {
        'mean': np.mean(data),
        'median': np.median(data),
        'std': np.std(data)
    }
    assert stats_report(data) == expected_output

def test_divide_inputs_are_numeric():
    number_1 = 'a'
    number_2 = 5
    with pytest.raises(TypeError):
        divide(number_1, number_2)

if __name__ == "__main__":
    pytest.main() # This will run the tests in this file, given that you have installed pytest.
