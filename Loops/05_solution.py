# find the first non repeated word
word = "teeth"

for char in word:
    if word.count(char) == 1:
        print(char)
        break