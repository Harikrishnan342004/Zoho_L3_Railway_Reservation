class Train:
    def __init__(self,capacity = 50):
        self.capacity  = capacity
        self.passengers = []
        self.waiting_list = []
    
    def book_ticket(self , passenger):
        if( len(self.passengers) < self.capacity ):
            self.passengers.append(passenger)
            print("Ticket Booked")
        else:
            self.waiting_list.append(passenger)
            print()



class Passenger:
    def __init__(self, name):
        self.name = name

    def main():
        train = Train()
        print("Welcome to Reservation system")


    while True:
        print("\n 1.Book Ticket \n 2.Cancel Ticket \n 3.Check_Pne \n 4.Exit")
        choice = int(input("Enter the Choice"))


        if( choice == "1"):
            name = input("enter the name")
            passenger = Passenger(name)
            train.book_ticket(passenger)



if __name__ == "__main__":
    main()