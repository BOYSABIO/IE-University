invoices = {}
collected = 0
pending = 0
more = ""

while more != "T":
    if more == "A":
        key = input("Enter invoice number: ")
        cost = float(input("Enter the cost of the invoice: "))
        invoices[key] = cost
        pending += cost
    if more == "P":
        key = input("Enter the number of the invoice to be paid: ")
        cost = invoices.pop(key, 0)
        collected += cost
        pending -= cost
    print("Collected: ", collected)
    print("Pending Collection: ", pending)
    more = input("Do you want to add a new invoice? (A), pay it (P), Terminate it (T): ")