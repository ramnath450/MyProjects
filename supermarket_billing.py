#Super Market Billing System
def supermarket_billing():
    while True:
        name = input("Enter name of Customer :")
        total_amount=0
        while True:
            quantity = int(input("Enter quantity of item :"))
            amount= float(input("Enter amount of item :"))
            total_amount += quantity*amount
            other_items = input("Do you want to add other items (y/n) :")
            if other_items.lower() == "n":
                break
        print(f"Name of customer :{name}")
        print(f"Total amount :{total_amount}")
        print("Thank you for shopping with us")
        next_person = input("Do you want to go to next person (y/n) :")
        if next_person.lower() == "n":
            break
    print("Thank you for visiting our supermarket")

if __name__ == "__main__":
    supermarket_billing()