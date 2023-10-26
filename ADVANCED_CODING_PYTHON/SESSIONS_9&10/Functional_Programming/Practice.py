def length_words(scentence):
    words = scentence.split()
    lengths = map(len, words)
    return dict(zip(words, lengths))

print(length_words("Welcome to Python"))