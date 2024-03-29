class Train:           #Two classs are definded in this program one is class Train ......... 
    #Tha contain capacity , passengers, waiting_list
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.passengers = []
        self.waiting_list = []

        # Attributes and methods of the classes are encapsulated within their respective classes.
        #  For example, capacity, passengers,
        #  and waiting_list are encapsulated within the Train class.
    
    def book_ticket(self, passenger):
        if ( len(self.passengers) < self.capacity):
            self.passengers.append(passenger)
            print("Ticket Booked")
        else:
            self.waiting_list.append(passenger)
            print("Train is full. Added to waiting list")
    
    def cancel_ticket(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(Passenger)
            print("Cannceled")
        elif passenger in self.waiting_list:
            self.passengers.remove(passenger)
            print("Cannceled from waiting list")
        else:
            print("Passenger not found")


    def print_pnr_details(self):
        print("Passengers with confirmed tickests:")
        for passenger in self.passengers:
            print(passenger.name)
        print("Passenger on waiting list:")
        for Passenger in self.waiting_list:
            print(passenger.name)


    
class Passenger:    # Another class is Passengers that contain passenger name Attributes
    def __init__(self, name):
        self.name = name


def main():
    train = Train()
    print("Welcome to Ticket Reservation System\n")
    
    while True:
        print("\n1. Book Ticket \n 2.Cancel Ticket \n 3.Print PNR Details \n 4.Exit")
        choice = input("Enter Passenger choice: ")

        if choice == "1":
            name = input("Enter passenger name: ")
            passenger = Passenger(name)
            train.book_ticket(passenger)
        
        elif choice == "2":
            name = input("enter passenger name: ")
            passenger = Passenger(name)
            train.cancel_ticket(passenger)
        elif choice == "3":
            train.print_pnr_details()
        elif choice == "4":
            print("Exiting...")
        else:
            print("Invalid choice. Please enter a valid option")



if __name__ == "__main__":
    main()
