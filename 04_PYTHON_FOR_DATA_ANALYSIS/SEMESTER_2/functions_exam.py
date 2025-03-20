import pandas as pd
from datetime import datetime
import re

def calendar(string1, string2):
    if not isinstance(string1, str):
        raise TypeError('The input must be a string')
    if not isinstance(string2, str):
        raise TypeError('The input must be a string')
    
    pattern_check = r'\d{4}-\d{2}-\d{2}'
    if not re.match(pattern_check, string1):
        raise ValueError("The input must be in the format 'YYYY-MM-DD'")
    if not re.match(pattern_check, string2):
        raise ValueError("The input must be in the format 'YYYY-MM-DD'")

    date1 = pd.to_datetime(string1)
    date2 = pd.to_datetime(string2)

    df = pd.DataFrame(
        {
            'DatetimeIndex': [pd.to_datetime(date1), pd.to_datetime(date2)],
            'day':[date1.day, date2.day],
            'month': [date1.month, date2.month],
            'year': [date1.year, date2.year],
            'day_of_week': [date1.day_of_week, date2.day_of_week],
            'is_weekend': [date1.day_name() in ['Saturday', 'Sunday'], date2.day_name() in ['Saturday', 'Sunday']],
            'quarter': [str(date1.year) + 'Q' + str(date1.quarter), str(date2.year) + 'Q' + str(date2.quarter)]
        }
    )
    return df.set_index('DatetimeIndex')

def analyze_text(list_of_strings):
    if not isinstance(list_of_strings, list):
        raise TypeError('The input must be a list')
    for i in list_of_strings:
        if not isinstance(i, str):
            raise ValueError('All elements in the list must be strings')

    vowel_pattern = r'[a, e, i, o, u]'
    consonant_pattern = r'[^aeiou\s]'

    dictionary = {}
    dictionary['text'] = [sentence for sentence in list_of_strings]
    dictionary['number_of_words'] = [len(list(sentence)) for sentence in list_of_strings]
    dictionary['number_of_vowels'] = [len(re.findall(vowel_pattern, sentence)) for sentence in list_of_strings]
    dictionary['number_of_consonants'] = [len(re.findall(consonant_pattern, sentence)) for sentence in list_of_strings]
    dictionary['number_of_unique_vowels'] = [len(set(re.findall(vowel_pattern, sentence))) for sentence in list_of_strings]
    dictionary['number_of_unique_consonants'] = [len(set(re.findall(consonant_pattern, sentence))) for sentence in list_of_strings]

    df = pd.DataFrame(dictionary)
    return df



if __name__ == '__main__':
    print(calendar('2025-01-01', '2025-01-02'))
    print(analyze_text(["Check, check, check, is this thing on?"]))
