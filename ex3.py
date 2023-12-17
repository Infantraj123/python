
available_seats = {
    "Economy": {"A1": True, "A2": False, "B1": True, "B2": True},
    "Business": {"C1": False, "C2": True, "D1": True, "D2": False}
}

def display_status():
    print("Class: Economy")
    print("Seat Status")
    for seat, status in available_seats["Economy"].items():
        print(f"{seat} {'Available' if status else 'Not Available'}")

    print("\nClass: Business")
    print("Seat Status")
    for seat, status in available_seats["Business"].items():
        print(f"{seat} {'Available' if status else 'Not Available'}")

def change_status(class_name, seat_no):
    if available_seats[class_name][seat_no]:
        available_seats[class_name][seat_no] = False
        print("Success. Booking Confirmed")
    else:
        print("Seat already booked")
