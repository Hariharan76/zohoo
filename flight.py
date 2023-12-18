class Flight:
    def __init__(self, flight_number, source, destination, departure_time, seats, price):
        self.flight_number = flight_number
        self.source = source
        self.destination = destination
        self.departure_time = departure_time
        self.seats = seats
        self.price = price

    def display_flight_info(self):
        print(f"Flight {self.flight_number}:")
        print(f"Source: {self.source}")
        print(f"Destination: {self.destination}")
        print(f"Departure Time: {self.departure_time}")
        print(f"Available Seats: {self.seats}")
        print(f"Price: ${self.price:.2f}")
        print()

class BookingSystem:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def display_available_flights(self):
        print("Available Flights:")
        for flight in self.flights:
            flight.display_flight_info()

    def book_flight(self, flight_number, num_passengers):
        for flight in self.flights:
            if flight.flight_number == flight_number:
                if flight.seats >= num_passengers:
                    flight.seats -= num_passengers
                    print(f"Booking successful for Flight {flight_number} for {num_passengers} passengers.")
                else:
                    print(f"Sorry, there are not enough seats available on Flight {flight_number}.")
                return
        print(f"Flight {flight_number} not found.")

def main():
    booking_system = BookingSystem()

    flight1 = Flight("AA101", "New York", "Los Angeles", "10:00 AM", 100, 250.00)
    flight2 = Flight("UA202", "Chicago", "Miami", "12:30 PM", 75, 180.00)
    flight3 = Flight("DL303", "San Francisco", "Seattle", "2:15 PM", 50, 150.00)

    booking_system.add_flight(flight1)
    booking_system.add_flight(flight2)
    booking_system.add_flight(flight3)

    while True:
        print("\nFlight Booking System")
        print("1. Display Available Flights")
        print("2. Book a Flight")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            booking_system.display_available_flights()
        elif choice == '2':
            flight_number = input("Enter the flight number: ")
            num_passengers = int(input("Enter the number of passengers: "))
            booking_system.book_flight(flight_number, num_passengers)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
