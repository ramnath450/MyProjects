# Define the menu of restaurant

menu = {
"Pizza":40,
"Pasta":50,
"Burger":60,
"Salad":70,
"Coffee":80
}
print("Welcome to our restaurant!")
print("Here is our menu:")
for item in menu:
    print(item, ":", menu[item])
order_total=0

item_1 = input("Enter the first item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Sorry, {item_1} is not available on our menu.")
while True:
    another_order = input("Do you want to order another item? (yes/no) ")
    if another_order.lower()=="yes":
        item_2=input("Enter the second item you want to order: ")
        if item_2 in menu:
            order_total+=menu[item_2]
            print(f"Your item {item_2} has been added to your order")
        else:
            print(f"Sorry, {item_2} is not available on our menu")
            break
    else:
        break   
print(f"Your total order is {order_total}")