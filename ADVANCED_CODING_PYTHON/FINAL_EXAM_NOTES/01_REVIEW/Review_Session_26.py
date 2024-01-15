def main():
    infileName = input("Please enter a file: ") + ".txt"

    infile = open(infileName, "r")
    selection = input("Please select '1' to save the conversions in a file or '2' to display them: ")

    if selection == "1":
        outfileName = input("What file should the conversions go into?: ") + ".txt"
        outfile = open(outfileName, 'w')

        for number in infile:
            numberGallons = float(number) * 3.78541
            print(round(numberGallons, 3), file=outfile)
        
        print("Numbers in Gallons written to", outfileName)
        outfile.close()
    else:
        print("\nFind below the conversions:\n")
        for number in infile:
            numberGallons = float(number) * 3.78541
            print(round(numberGallons, 3))

    infile.close()

main()