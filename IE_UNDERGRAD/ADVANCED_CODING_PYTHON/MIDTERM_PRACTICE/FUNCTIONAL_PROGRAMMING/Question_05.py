"""Write a function that receives a sentence and returns a dictionary with the words it containsand their length."""

#def converter(sentence):
    #list = sentence.split()
    #lengths = map(len, list)
    #return dict(zip(sentence, lengths))

def word_lengths(sentence):
    return {word:len(word) for word in sentence.split()}

sentence = input("Please enter a scentence: ")
#print(converter(sentence))
print()
print(word_lengths(sentence))