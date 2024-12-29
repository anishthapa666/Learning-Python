# to make a pyramid shape
row  =5
for i in range(5):
    for s in range(-6,-i):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print("")
    