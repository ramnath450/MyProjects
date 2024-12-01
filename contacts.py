contacts = {}

while True:

    print("\nContact Book App")
    print("1. Create Contact")
    print("2. View Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Seacrh Contact")
    print("6. Count Contact")
    print("7. Exit")

    choice = int(input("Enter your choice: "))
    if choice ==1:
        name = input("Enter the name: ")
        if name in contacts:
            print(f"Contact {name} name already exists")
        else:
            age = int(input("Enter the age: "))
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            contacts[name] = {"age": age, "phone": phone, "email": email}
            print(f"Contact {name} created successfully")

    elif choice==2:
        name = input("Enter the name: ")
        if name in contacts:
            print("Name: ", name)
            print("Age: ", contacts[name]["age"])
            print("Phone: ", contacts[name]["phone"])
            print("Email: ", contacts[name]["email"])
        else:
            print(f"Contact {name} not found")

    elif choice==3:
        name = input("Enter the name: ")
        if name in contacts:
            age = int(input("Enter the age: "))
            phone = input("Enter the phone number: ")
            email = input("Enter the email: ")
            contacts[name] = {"age": age, "phone": phone, "email": email}
            print(f"Contact {name} updated successfully")

        else:
            print(f"Contact {name} not found")

    elif choice==4:
        name = input("Enter the name: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted successfully")
        else:
            print(f"Contact {name} not found")

    elif choice==5:
        name = input("Enter the name: ")
        if name in contacts:
            print("Name: ", name)
            print("Age: ", contacts[name]["age"])
            print("Phone: ", contacts[name]["phone"])
            print("Email: ", contacts[name]["email"])

        else:
            print(f"Contact {name} not found")

    elif choice==6:
        print("Total contacts: ", len(contacts))

    elif choice==7:
        print("Exiting the app")
        break

    else:
        print("Invalid choice")


        