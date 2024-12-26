#lets orders our chiya...
print("Welcome to our tea shop... What whould you like have today ")

my_menu = ["seto_chiya" ,"kalo_chiya" ,"masala_chiya", "milk"]


print(my_menu)
def chiya(n):
    if n==1:
       print("Here is your seto_chiya")
    elif n==2:
       print("Here is your kalo_chiya")
    elif n==3 :
       print("Here is your masala_chiya")
    elif n==4 :
       print("Here is your milk" )

order_no = int(input("Enter the number of your order"))

chiya(order_no)

print("paisa natri gais vaney marxas ")