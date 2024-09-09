def main():
    f = open("greeting.txt", "r")
    
    print(f.read()) #When you print this way it is all one long string but it reads the \n and returns
    print()
    
    f = open("greeting.txt", "r")
    lines = f.readlines()
    print(lines) #\n is a character

    # Closing a file:
    f.close()

main()