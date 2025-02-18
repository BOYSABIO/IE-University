# * If the script is executed from the command line, it should print:
#  * Current date and time
#  * "Executed from the command line by {username}"
# * If the script is imported, it should print:
#  * Current date and time
#  * "Imported from {filename}"

import sys
import datetime

filename = sys.argv[0]
username = sys.argv[1]


def print_current_date_and_time():
    print(datetime.datetime.now())


def print_message_executed(username):
    print(f"Executed from the command line by {username}")


def print_message_imported():
    print(f"Imported from {filename}")


if __name__ == "__main__":
    print_current_date_and_time()
    print_message_executed(username)
else:
    print_current_date_and_time()
    print_message_imported()
