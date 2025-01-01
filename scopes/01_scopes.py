def func1(num):
    def func2(x):
        return x**num
    return func2

y = func1(1)
print(y(8))