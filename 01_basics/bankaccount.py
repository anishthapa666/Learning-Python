class bank():
    def __init__(self,name,initial_amount = 0):
        self.name = name
        self.balance = initial_amount
    
    def deposit(self,amount):
        self.balance+=amount
        print(f"you have entered rs {amount} in your account")
        print(f"\n your new balance is {self.balance}")
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient amount")
        else:
            self.balance-=amount
            print("\n your new balance is {self.balance}")
    def info(self):
        print(f"MR {self.name} have {self.balance} in their account")

def main():
        print("\n welcome to our account management system")
        name= input("enter the name of the account holder")
        balance = float(input("enter the initial balance of the account holder."))
        account = bank(name,balance)
        while True:
            print("\n chose an option")
            print("1. deposit")
            print("2. withdraw")
            print("3. show info")
            print("4. Exit")
            choice = int(input("Which one would you choose: "))
            
            match choice:
                case 1:
                    amount =float(input("Enter the amount you want to deposit"))
                    account.deposit(amount)
                case 2:
                    amount = float(input("Enter the amount you to withdraw."))
                    account.withdraw(amount)
                case 3:
                    account.info()
                case 4:
                    break
                case _:
                    print("Invalid choice")
 
if __name__ == "__main__":
    main()