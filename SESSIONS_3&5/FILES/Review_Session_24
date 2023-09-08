def main():
    fileName = input("Please enter your filename: ") + ".txt"
    line = 0
    word = 0
    char = 0

    openFile = open(fileName, "r")
    for file_lines in openFile:
        line += 1
        word = file_lines.count(" ") + 1 + word
        char = len(file_lines) + char - 1
    char += 1

    print("Your file has", line, "lines.")
    print("Your file has", word, "words.")
    print("Your file has", char, "characters.")

main()