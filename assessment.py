class TrainCoach:
    def __init__(self):
        # Initializing the coach with 80 seats
        self.seats = ['O'] * 77 + ['O', 'O', 'O']  # Last row has only 3 seats
        self.booked_seats = {5, 10, 15, 30, 31, 32}  # Predefined booked seats
        for seat in self.booked_seats:
            self.seats[seat] = 'X'  # 'X' represents booked seats

    def display_seats(self):
        # Display seat availability
        print("Seat Status:")
        for i in range(11):
            print(" ".join(self.seats[i*7:(i+1)*7]), f"({i*7 + 1}-{(i + 1) * 7})")

    def book_seats(self, num_seats):
        if num_seats < 1 or num_seats > 7:
            print("You can only book between 1 to 7 seats.")
            return

        # Try to book seats in rows first
        for i in range(len(self.seats)):
            if self.seats[i] == 'O':
                # Check if there are enough contiguous available seats
                if all(self.seats[j] == 'O' for j in range(i, min(i + num_seats, len(self.seats)))):
                    # Book the seats
                    for j in range(i, i + num_seats):
                        self.seats[j] = 'X'
                    booked_seat_numbers = [j + 1 for j in range(i, i + num_seats)]
                    print(f"Booked Seats: {booked_seat_numbers}")
                    return

        # If no row has enough contiguous seats, look for nearby seats
        available_seats = []
        for i in range(len(self.seats)):
            if self.seats[i] == 'O':
                available_seats.append(i + 1)
                if len(available_seats) == num_seats:
                    # Book the nearby seats
                    for seat_number in available_seats:
                        self.seats[seat_number - 1] = 'X'
                    print(f"Booked Nearby Seats: {available_seats}")
                    return

        print("Sorry, not enough seats available to book.")

if __name__ == "__main__":
    coach = TrainCoach()

    while True:
        coach.display_seats()
        try:
            num_seats = int(input("Enter number of seats to book (1-7 or 0 to exit): "))
            if num_seats == 0:
                print("Exiting the booking system.")
                break
            coach.book_seats(num_seats)
        except ValueError:
            print("Please enter a valid number.")









