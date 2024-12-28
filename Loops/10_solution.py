import time

wait_time = 1
max_retries = 5
attempt = 0
while attempt < max_retries:
    print("attempt", attempt + 1,"-wait_time" , wait_time)
    attempt+=1
    time.sleep(wait_time)
    wait_time *=2