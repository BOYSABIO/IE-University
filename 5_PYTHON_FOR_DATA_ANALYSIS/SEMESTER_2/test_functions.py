import functions 
import pytest
import pandas as pd

def test_get_financial_data_returns_df():

    stock_ticker = 'GOOG'
    start_date = '2025-01-01'
    end_date = '2025-01-02'
    column_to_extract = 'Close'

    df = functions.get_financial_data(
        stock_ticker, 
        start_date, 
        end_date, 
        column_to_extract)
    
    empty_df = pd.DataFrame()
    
    assert len(df) > len(empty_df)

if __name__ == '__main__':
    pytest.main()