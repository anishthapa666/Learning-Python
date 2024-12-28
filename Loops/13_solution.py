vowels = ["a","e","i","o","u"]
count = 0
word = "Anish"
for i in word.lower():
    if i in vowels:
        count+= 1
print(count)