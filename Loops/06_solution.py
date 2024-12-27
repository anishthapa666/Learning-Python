# find factorial using loops while and for 
num = 8
fact = 1

# while num > 0:
#     fact = fact * num
#     num = num-1

for i in range(1,num + 1):
    fact *= i

print(fact)