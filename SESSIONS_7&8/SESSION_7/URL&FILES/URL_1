# Function that recieves URL of a text file and returns the number of words contained
# Parameters: URL is a string ith the url of the text file
# Returns: Number of words contained in the text file within the URL
def count_words(url):
    from urllib import request
    from urllib.error import URLError # Exception handling

    try:
        f = request.urlopen(url)
    except URLError:
        return("The URL " + url + " does not exist")
    else:
        content = f.read()
        return len(content.split())
    
print(count_words("https://www.gutenberg.org/files/2000/2000-0.txt"))
print(count_words("https://there_is_no_file.txt"))