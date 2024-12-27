# keep asking for user until they give number between 1 and 10


while True :
    num = int(input("Enter a number between 1 to 10: "))
    if num in range(1,11):
        print("Thanks for enter the correct number.")
        break
    else:
        print("You have entered the wrong number , please try again")
