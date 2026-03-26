import yfinance as yf
import re
import datetime

def end_date_greater_than_start_date(start_date, end_date):
    return start_date < end_date

def check_date_format(date_string):
    desired_format = re.compile(r'^\d{4}-\d{2}-\d{2}$')
    return desired_format.match(date_string).group() == date_string

def get_financial_data(stock_ticker, start_date, end_date, column_to_extract):

    if not isinstance(stock_ticker, str):
        raise TypeError('stock_ticker is not a string')
    
    if not isinstance(start_date, str):
        raise TypeError('start_date is not a string')
        
    if not isinstance(end_date, str):
        raise TypeError('end_date is not a string')
    
    if not check_date_format(start_date):
        raise ValueError('The start_date is not in the correct format YYYY-MM-DD')
    
    if not check_date_format(end_date):
        raise ValueError('The end_date is not in the correct format YYYY-MM-DD')
    
    if not end_date_greater_than_start_date(start_date, end_date):
        raise ValueError('The start_date is not greater than the end_date')
    
    data = yf.download(stock_ticker, start_date, end_date)
    
    return data[[column_to_extract]]


if __name__ == '__main__':
    pass