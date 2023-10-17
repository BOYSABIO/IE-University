def finder(list, tin, month):
    count = 0
    for i in list:
        if i.get('month') == month & i.get('nif') == tin:
            count +=1
    
    dictionary = {month:count}
    return dictionary

invoices = [{'nif': 'B12345678', 
             'month': 'March', 
             'amount':1000, 
             'vat': 10},
            {'nif': 'A98765432', 'month': 'July', 'amount':500, 'vat': 21},
            {'nif': 'B12345678', 'month': 'March', 'amount':2000, 'vat': 21},
            {'nif': 'C02040506', 'month': 'January', 'amount':200, 'vat': 4},
            {'nif': 'A98765432', 'month': 'July', 'amount':1500, 'vat': 10},
            {'nif': 'B12345678', 'month': 'April', 'amount':600, 'vat': 10},
            {'nif': 'B12345678', 'month': 'March', 'amount':100, 'vat': 4}]

tin = input("Please enter the tin you would like to check: ")
month = input("Please enter the month you would like to check: ")

finder(invoices, tin, month)
