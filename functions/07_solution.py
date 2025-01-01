# about *args- it allows us to pass as many arguments we like...

def sum_all(*args):
    for i in args:
        print(i*2)


    return sum(args)

print(sum_all(2,4,5,6))
