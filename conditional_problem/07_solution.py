# checking the strenght of the pasword
password = str(input("enter the password: "))

num = len(password)

if num < 6:
   strength = "weak"
elif num <= 10:
    strength = "medium"
elif num >10:
    strength = "strong"
print(strength)
