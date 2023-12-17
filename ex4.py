from ex3 import display_status, change_status

while True:
    print("\n1. Display Status\n2. Change Status")
    choice = input("Enter your Choice (1/2): ")

    if choice == '1':
        display_status()
    elif choice == '2':
        class_name = input("Enter Class: ")
        seat_no = input("Enter Seat No: ")
        change_status(class_name, seat_no)
    else:
        print("Invalid choice. Exiting...")
        break
