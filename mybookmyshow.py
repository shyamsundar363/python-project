class MyBookMyShow:
    def __init__(self,row,column):
        self.rows = row
        self.columns = column
        self.no_seats = self.rows * self.columns
        self.seats = []
        self.viewers = {}
        self.total_earnings = 0
        self.current_earning = 0
        self.create_seats()
    def print_seats(self):
        for col in range(0,self.columns+1):
            if col == 0:
                print("  ",end=" ")
            else:
                print(col,end = " ")
        print("")
        for seats in self.seats:
            for seat in seats:
                if len(seat) < 10:
                    print(seat,end = " ")
                else:
                    print(seat,end = "  ")
            print("")
    def create_seats(self):
        seat = []
        for row in range(1,self.rows+1):
            if row < 10:
                seat.append(f" {row}")
            else:
                seat.append(f"{row}")
            for num in range(1,self.columns+1):
                seat.append("S")
                if num % self.columns == 0:
                    self.seats.append(seat)
                    seat = []
    def book_ticket(self,row,column):
        if self.statistics() != self.rows*self.columns:
            try:
                if self.seats[row -1][column] == "S":
                    cost = self.cost_of_ticket(row,column)
                    print(f"Ticket cost: {cost}")
                    if input("Do you want to confirm booking?(yes/no)").lower() == "yes":
                        self.get_user_details(row,column)
                        self.seats[row-1][column] = "B"
                        self.total_earnings += cost
                        self.current_earning = cost
                    else:
                        pass
            except IndexError:
                print("Sorry seat is not available")
        else:
            print("Sorry Housefull :(")
    
    
    def statistics(self):
        ticket_sold = 0
        for seat in self.seats:
            ticket_sold += seat.count("B")
        percentage = (ticket_sold / self.no_seats) * 100
        return ticket_sold,percentage,self.total_earnings,self.current_earning
    
    def get_user_details(self,row,col):
        viewer_details = {}
        viewer_details["name"] = input("Name: ")
        viewer_details["age"] = input("Age: ")
        viewer_details["gender"] = input("Gender: ")
        viewer_details["phone"] = input("Mobile Number: ")
        self.viewers[(row,col)] = viewer_details
    
    
    def print_user_details(self,row,column):
        return self.viewers[(row,column)]
    
    def cost_of_ticket(self,row,column):
        if self.no_seats < 60:
            cost = 10
        else:
            if row * column < self.no_seats // 2:
                cost = 10
            else:
                cost = 8
        return cost