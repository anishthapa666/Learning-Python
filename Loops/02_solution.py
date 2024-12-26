# to find sum of even number till nth term
num = 9
sum = 0
for i in range(0,num+1):
    if i%2==0:
        sum+=i
print("sum to the nth term  is", sum)