1.
# One application will be given. Time: 2h30m
# Write an application for booking railway ticket reservation system. The application should have four functionalities.
# 1.	Book
# 2.	Cancel
# 3.	Print booked tickets (details with summary)
# 4.	Print available tickets (details with summary)
# Conditions for booking:
# There are a total of 63 berths for 63 confirmed tickets, 9 berths for 18 RAC tickets and 10 tickets in waiting-list. If the waiting-list ticket count goes above 10, print as ‘No tickets available’. The following passenger details should be obtained from the user.
# 1.	Name
# 2.	Age
# 3.	Gender
# 4.	Berth Preference
# The tickets should not be allocated for children below age 5.But, their details should be stored. Lower berth should be allocated for persons whose age is above 60 and ladies with children if available. Side-lower berths should be allocated for RAC passengers.
# Conditions for cancelling:
# Whenever a ticket is cancelled, a ticket from RAC should be confirmed and a waiting-list ticket should move to RAC.
# Conditions for printing booked tickets:
# Print all the tickets that are filled along with the passenger details and at the end, print the total number of tickets that are filled.
# Conditions for printing available tickets:
# Print all the tickets that are unoccupied and at the end, print the total number of tickets that are unoccupied.

class passenger:
    def __init__(self,name,age,gender,berth_preference):
        self.name=name
        self.gender=gender
        self.age=age
        self.berth_perference=berth_preference
class Railway_system:
    def __init__(self):
        self.total_tickets=63
        self.Rac_tickets=18
        self.waitingtickets=10
        self.conformed_tickets=[]
        self.rac_tickets = []
        self.waiting_list = []
        
    def booking(self):
        name=input("enter the name:")
        gender=input("enter the gender(M/F):").lower()
        age=int(input("enter the age:"))
        berth_perference=input("enter the berth pererence(lower/upper/middle):").lower()        
        if age<5:
            print("dont take ticket in child")
            return
        if berth_perference == "lower" and age <= 60 or gender == 'f' and age <=18:            
            berth_perference="LOWER"              
        else: 
            berth_perference="side-LOWER" 
        if len(self.conformed_tickets)< self.total_tickets:
            person=passenger(name,age,gender,berth_perference)
            self.conformed_tickets.append(person)
            print("the tickets booking was sucessfully ")
            return
        elif len(self.rac_tickets)<self.rac_tickets:
            person=passenger(name,age,gender,berth_perference="rac berth")
            self.conformed_tickets.append(person)
            print("the tickets rac booking was sucessfully ")
            return
        elif len(self.waiting_list)<self.waitingtickets:
            person=passenger(name,age,gender,berth_perference="waiting list")
            self.conformed_tickets.append(person)
            print("the tickets booking in  waitinglist")
            
        else:
            print("no tickets available")
    def cancel_tickets(self):
        if len(self.rac_tickets)>0:
            self.conformed_tickets.append(self.rac_tickets.pop(0))
        if len(self.waiting_list)>0:
                self.rac_tickets.append(self.conformed_tickets.pop(0))
        print("your ticket was cancel suceesfully")
    def booked_tickets(self):
        print("Booked Tickets:")
        for i, passenger in enumerate(self.conformed_tickets):
            print(f"Ticket {i + 1}: Name: {passenger.name}, Age: {passenger.age}, Gender: {passenger.gender}, Berth: {passenger.berth_preference}")
        print(f"Total booked tickets: {len(self.conformed_tickets)}")

    def avialable_tickets(self):
        print("avaialbe tickets")
        for i in range(self.total_tickets-len(self.conformed_tickets)):
            print(f"berth Ticket{i+1} is avialable")
        for i in range(self.Rac_tickets-len(self.rac_tickets)):
            print(f"Rac Ticket{i+1} is avialable")
        for i in range(self.waitingtickets-len(self.waiting_list)):
            print(f"waiting Ticket{i+1} is avialable")
                
                
if __name__ == "__main__":
    ticket_system=Railway_system()
    
    while True:
        print("1:booking")
        print("2:cancel_tickets")
        print("3:booked_Tickets")
        print("4:avialable_Tickets")        
        ina=int(input("enter your choice:"))
        if ina==1:
            ticket_system.booking()
        elif ina==2:
            ticket_system.cancel_tickets()
        elif ina ==3:
            ticket_system.booked_tickets()
        elif ina ==4:
            ticket_system.avialable_tickets()
            break
        else:
            print("print correct choice")
        