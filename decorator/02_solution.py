import time
def caches(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
        

    return wrapper



# def book(name , pages):
#     print(f"{name} of {pages} pg")
@caches
def long(a,b):
    time.sleep(4)
    return a*b

print(long(4,5))
print(long(4,5))

# book("oop","100")

