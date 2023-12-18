import random

class Car:
    def __init__(self, registration_number, user):
        self.registration_number = registration_number
        self.user = user

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

class ParkingLot:
    def __init__(self, total_floors, floors, slots_per_floor):
        self.total_floors = total_floors
        self.floors = floors
        self.slots_per_floor = slots_per_floor
        self.available_slots = [[True] * slots_per_floor for _ in range(total_floors)]
        self.car_registry = {}
        self.queue = []

    def register_car(self, registration_number, user):
        if registration_number in self.car_registry:
            return "Car already registered."
        
        for floor in range(self.total_floors):
            for slot in range(self.slots_per_floor):
                if self.available_slots[floor][slot]:
                    self.available_slots[floor][slot] = False
                    car = Car(registration_number, user)
                    self.car_registry[registration_number] = (floor, slot)
                    return f"Car {registration_number} registered on Floor {floor + 1}, Slot {slot + 1}."
        
        self.queue.append((registration_number, user))
        return "Parking lot is full. Car added to the queue."

    def assign_parking(self):
        if not self.queue:
            return "No cars in the queue."

        registration_number, user = self.queue.pop(0)
        return self.register_car(registration_number, user)

    def calculate_cost(self, registration_number, hours_parked):
        if registration_number not in self.car_registry:
            return "Car not found."

        # Implement cost calculation logic here

    def generate_report(self):
        # Implement report generation logic here
        pass

# Usage example
if __name__ == "__main__":
    user1 = User(1, "John")
    user2 = User(2, "Alice")

    parking_lot = ParkingLot(total_floors=3, floors=3, slots_per_floor=10)

    print(parking_lot.register_car("ABC123", user1))
    print(parking_lot.register_car("XYZ789", user2))
    print(parking_lot.assign_parking())
