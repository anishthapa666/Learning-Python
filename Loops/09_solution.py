# To check uniqness of list
fruits = ["apple","banana","orange","apple"]
unique_f = set()
for item in fruits:
    if item in unique_f:
        print("duplicate ",item)
        break
    else:
        unique_f.add(item)
