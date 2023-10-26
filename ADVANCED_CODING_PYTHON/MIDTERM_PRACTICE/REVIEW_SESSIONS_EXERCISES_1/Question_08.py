"""IBAN (International Bank Account Number) is an internationally agreed system of identifying bank 
accounts across national borders to facilitate the communication and processing of cross border 
transactions with a reduced risk of transcription errors. It has a standard length of 22 alphanumeric 
characters, comprising:
    o Country Code (2 digits)
    o Check Number (2 digits)
    o Bank Identifier (4 digits)
    o Sort Code (6 digits) Account Number (8 digits)

Create an "IBAN processor" program that:
    • Gets an IBAN (string of numbers and letters) as input
    • Ensures the IBAN is of the proper length (22 characters) and if it is NOT theproper length, 
    requests the user to re-enter a valid IBAN
    • Prints out each of the parts of the IBAN separately"""



required_length = 22

country_code = 0
check_number = 0
bank_identifier = 0
sort_code = 0
account_number = 0

iban = input("Please enter Iban (Do not include spaces): ")

if len(iban) == required_length:
    print('Country code:', iban[:2])
    print('Check number:', iban[2:4])
    print('Bank Identifier:', iban[4:8])
    print('Sort code:', iban[8:14])
    print('Account number:', iban[14:22])
else:
    print("Your Iban is the incorrect length")

# GB 12 ABCD 890111 11167800

