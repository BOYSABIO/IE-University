import functions 
import pytest
import pandas as pd
import yfinance as yf

def test_get_financial_data_returns_df():

    stock_ticker = 'GOOG'
    start_date = '2025-01-01'
    end_date = '2025-01-31'
    column_to_extract = 'Close'

    df = functions.get_financial_data(
        stock_ticker, 
        start_date, 
        end_date, 
        column_to_extract)
    
    empty_df = pd.DataFrame()
    
    assert len(df) > len(empty_df)

def test_get_financial_data_stock_ticker_not_a_string():
    stock_ticker = 123
    start_date = '2025-01-01'
    end_date = '2025-01-31'
    column_to_extract = 'Close'
    
    with pytest.raises(TypeError):
        df = functions.get_financial_data(
        stock_ticker, 
        start_date, 
        end_date, 
        column_to_extract)

def test_get_financial_data_date_wrong_format():
    stock_ticker = 'GOOG'
    start_date = '01-01-2025'
    end_date = '2025-01-31'
    column_to_extract = 'Close'

    with pytest.raises(AttributeError):
        functions.get_financial_data(stock_ticker, start_date, end_date, column_to_extract)

if __name__ == '__main__':
    pytest.main()