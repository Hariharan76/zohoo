class RailwayReservation:
    def __init__(self, total_seats):
        self.total_seats = total_seats
        self.available_seats = {seat: True for seat in range(1, total_seats + 1)}

    def display_available_seats(self):
        print("Available Seats:")
        for seat, status in self.available_seats.items():
            if status:
                print(f"Seat {seat} is available.")
            else:
                print(f"Seat {seat} is booked.")

    def book_seat(self, seat_number):
        if seat_number in self.available_seats and self.available_seats[seat_number]:
            self.available_seats[seat_number] = False
            print(f"Seat {seat_number} is booked successfully.")
        else:
            print(f"Seat {seat_number} is not available or already booked.")

    def cancel_seat(self, seat_number):
        if seat_number in self.available_seats and not self.available_seats[seat_number]:
            self.available_seats[seat_number] = True
            print(f"Seat {seat_number} is canceled successfully.")
        else:
            print(f"Seat {seat_number} is not booked or does not exist.")

def main():
    total_seats = 10  # Change this to the total number of seats in your railway compartment
    reservation_system = RailwayReservation(total_seats)

    while True:
        print("\nRailway Reservation System")
        print("1. Display available seats")
        print("2. Book a seat")
        print("3. Cancel a seat")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            reservation_system.display_available_seats()
        elif choice == "2":
            seat_number = int(input("Enter the seat number you want to book: "))
            reservation_system.book_seat(seat_number)
        elif choice == "3":
            seat_number = int(input("Enter the seat number you want to cancel: "))
            reservation_system.cancel_seat(seat_number)
        elif choice == "4":
            print("Thank you for using the Railway Reservation System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
