import time

def timmer(func):
    def wrappe(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"{func.__name__ }ran in {end -start}")
        return result
    return wrappe

@timmer
def delay(n):
    time.sleep(n)

delay(2)