# To find if the the year is leap year or not 
year = 2023
if year%4==0:
    if year%400==0 :
        print("leap year")
    elif year%100==0:
        print("Its not a leap year.")
    else:
        print("It is  a leap year.")
else:
    print("its not a leap year.")