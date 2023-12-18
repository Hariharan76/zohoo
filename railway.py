class Passenger:
    def __init__(self, name, age, gender, berth_preference):
        self.name = name
        self.age = age
        self.gender = gender
        self.berth_preference = berth_preference


class TicketReservationSystem:
    def __init__(self):
        self.total_confirmed_berths = 63
        self.total_rac_berths = 9
        self.total_waiting_list_tickets = 10
        self.confirmed_tickets = []
        self.rac_tickets = []
        self.waiting_list = []

    def book_ticket(self):
        if len(self.confirmed_tickets) < self.total_confirmed_berths:
            name = input("Enter passenger name: ")
            age = int(input("Enter passenger age: "))
            gender = input("Enter passenger gender (M/F): ")
            berth_preference = input("Enter berth preference (Lower/Upper/Middle): ").lower()

            if age < 5:
                print("Children below 5 years are not allowed to book tickets.")
                return

            if age >= 60 or (gender == 'f' and age >= 18):
                if berth_preference == 'lower':
                    berth_preference = 'Lower'
                else:
                    berth_preference = 'Side-Lower'

            if len(self.confirmed_tickets) < self.total_confirmed_berths:
                passenger = Passenger(name, age, gender, berth_preference)
                self.confirmed_tickets.append(passenger)
                print("Ticket booked successfully!")
            else:
                if len(self.rac_tickets) < self.total_rac_berths:
                    passenger = Passenger(name, age, gender, 'Side-Lower')
                    self.rac_tickets.append(passenger)
                    print("Ticket booked in RAC.")
                else:
                    if len(self.waiting_list) < self.total_waiting_list_tickets:
                        passenger = Passenger(name, age, gender, 'Waiting List')
                        self.waiting_list.append(passenger)
                        print("Ticket added to the waiting list.")
                    else:
                        print("No tickets available.")

    def cancel_ticket(self):
        if len(self.rac_tickets) > 0:
            self.confirmed_tickets.append(self.rac_tickets.pop(0))
        if len(self.waiting_list) > 0:
            self.rac_tickets.append(self.waiting_list.pop(0))
        print("Ticket cancelled and reallocated.")

    def print_booked_tickets(self):
        print("Booked Tickets:")
        for i, passenger in enumerate(self.confirmed_tickets):
            print(f"Ticket {i + 1}: Name: {passenger.name}, Age: {passenger.age}, Gender: {passenger.gender}, Berth: {passenger.berth_preference}")
        print(f"Total booked tickets: {len(self.confirmed_tickets)}")

    def print_available_tickets(self):
        print("Available Tickets:")
        for i in range(self.total_confirmed_berths - len(self.confirmed_tickets)):
            print(f"Ticket {i + 1}: Berth: Lower")
        for i in range(self.total_rac_berths - len(self.rac_tickets)):
            print(f"Ticket {i + 1}: Berth: Side-Lower")
        for i in range(self.total_waiting_list_tickets - len(self.waiting_list)):
            print(f"Ticket {i + 1}: Berth: Waiting List")
        print(f"Total available tickets: {self.total_confirmed_berths - len(self.confirmed_tickets) + self.total_rac_berths - len(self.rac_tickets) + self.total_waiting_list_tickets - len(self.waiting_list)}")


if __name__ == "__main__":
    ticket_system = TicketReservationSystem()

    while True:
        print("\nRailway Ticket Reservation System")
        print("1. Book")
        print("2. Cancel")
        print("3. Print Booked Tickets")
        print("4. Print Available Tickets")
        print("5. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            ticket_system.book_ticket()
        elif choice == 2:
            ticket_system.cancel_ticket()
        elif choice == 3:
            ticket_system.print_booked_tickets()
        elif choice == 4:
            ticket_system.print_available_tickets()
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please try again.")
