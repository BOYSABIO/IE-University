from urllib import request
def main():
    f = request.urlopen("https://........")
    data = f.read()
    print(data.decode("uft-8"))

main()