def menu():
    print("\n--- Railway Reservation System ---")
    print("1. Check Seat Availability")
    print("2. Book Ticket")
    print("3. View Reservation")
    print("4. Cancel Ticket")
    print("5. Exit")

seats = 5
bookings = []

while True:
    menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        print(f"Available seats: {seats}")

    elif choice == '2':
        if seats > 0:
            name = input("Enter your name: ")
            bookings.append(name)
            seats -= 1
            print("Ticket booked successfully!")
        else:
            print("No seats available")

    elif choice == '3':
        if bookings:
            print("Reservations:")
            for b in bookings:
                print("-", b)
        else:
            print("No reservations found")

    elif choice == '4':
        name = input("Enter name to cancel: ")
        if name in bookings:
            bookings.remove(name)
            seats += 1
            print("Ticket cancelled")
        else:
            print("Booking not found")

    elif choice == '5':
        print("Thank you!")
        break

    else:
        print("Invalid choice")
