# Manage Customer Database Company
# Datatype = dictionary

# Initialize an empty customer database as a dictionary
customer_database = {}

# Function to add a customer to the database
def add_customer():
    tin = input("Enter TIN number: ")
    name = input("Enter customer name: ")
    address = input("Enter customer address: ")
    telephone = input("Enter customer telephone: ")
    email = input("Enter customer email: ")
    preferred = input("Is this a preferred customer? (True/False): ").lower() == "true"
    
    customer_data = {
        "name": name,
        "address": address,
        "telephone": telephone,
        "email": email,
        "preferred": preferred
    }
    
    customer_database[tin] = customer_data
    print(f"Customer with TIN {tin} added successfully.")

# Function to remove a customer from the database
def remove_customer():
    tin = input("Enter TIN number to remove customer: ")
    if tin in customer_database:
        del customer_database[tin]
        print(f"Customer with TIN {tin} removed successfully.")
    else:
        print(f"Customer with TIN {tin} not found in the database.")

# Function to show customer details
def show_customer():
    tin = input("Enter TIN number to show customer details: ")
    if tin in customer_database:
        customer = customer_database[tin]
        print("Customer Details:")
        print(f"TIN: {tin}")
        print(f"Name: {customer['name']}")
        print(f"Address: {customer['address']}")
        print(f"Telephone: {customer['telephone']}")
        print(f"Email: {customer['email']}")
        print(f"Preferred: {customer['preferred']}")
    else:
        print(f"Customer with TIN {tin} not found in the database.")

# Function to list all customers
def list_all_customers():
    print("List of all customers:")
    for tin, customer in customer_database.items():
        print(f"TIN: {tin}, Name: {customer['name']}")

# Function to list preferred customers
def list_preferred_customers():
    print("List of preferred customers:")
    for tin, customer in customer_database.items():
        if customer['preferred']:
            print(f"TIN: {tin}, Name: {customer['name']}")

# Main program loop
def main():
    while True:
        print("\nMenu:")
        print("1. Add client")
        print("2. Remove client")
        print("3. Show client")
        print("4. List all clients")
        print("5. List preferred clients")
        print("6. Finish")
        
        choice = input("Enter your choice (1/2/3/4/5/6): ")
        
        if choice == '1':
            add_customer()
        elif choice == '2':
            remove_customer()
        elif choice == '3':
            show_customer()
        elif choice == '4':
            list_all_customers()
        elif choice == '5':
            list_preferred_customers()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select a valid option.")

main()