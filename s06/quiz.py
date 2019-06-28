f = open("poem.txt", "r")
text = f.read()
words= text.split()
print(words)
unique= set(words)




print(unique)
print(len(words))

print(len(unique))

def word_frequncy(text):
    frequency= {
        "unique":
    }
