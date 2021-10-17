from mybookmyshow import MyBookMyShow
row = int(input("How many rows? "))
column = int(input("How many columns? "))

my_movie = MyBookMyShow(row,column)
loop = True
while loop:
    user_choice = input("\n1. Print seats\n2. Buy a Tiket\n3. Statistis\n4. View User details.\n0. Exit\n")
    if user_choice == "1":
        my_movie.print_seats()
    elif user_choice == "0":
        loop = False
    elif user_choice == "2":
        book_row = int(input("Which Row: "))
        book_column = int(input("Which Column: "))
        my_movie.book_ticket(book_row,book_column)
    elif user_choice == "3":
        ticket_sold = my_movie.statistics()
        percentage = "{:.2f}".format(ticket_sold[1])
        print(f"Tickets Sold: {ticket_sold[0]}")
        print(f"Percentage: {percentage}%")
        print(f"Total Earnings: {ticket_sold[2]}")
        print(f"Current Earning: {ticket_sold[3]}")
    elif user_choice == "4":
        row = int(input("Which Row?: "))
        col = int(input("Which Col?: "))
        viewer = my_movie.print_user_details(row,col)
        print("\n========================================================")
        print(f'Name: {viewer["name"]}\nAge: {viewer["age"]}\nGender: {viewer["gender"]}\nPhone: {viewer["phone"]}')
        print("========================================================")