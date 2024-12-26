# Print the multiplication table for a given number up to ten except fitth iteration.
num = 7
for n in range(1,11):
    if n == 5:
        continue
    print(num,"X", n ,"=", n*num)
