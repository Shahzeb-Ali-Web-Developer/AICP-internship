class MountainRailway:
    def __init__(self):
        # Initialize data structures
        self.available_tickets = {"09:00": 6 * 80, "11:00": 6 * 80, "13:00": 6 * 80, "15:00": 6 * 80}
        self.total_passengers = {"09:00": 0, "11:00": 0, "13:00": 0, "15:00": 0}
        self.total_money = {"09:00": 0, "11:00": 0, "13:00": 0, "15:00": 0}

    def display_screen(self):
        # Display the current status of available tickets
        for hour, tickets in self.available_tickets.items():
            print(f"Train {hour}: {tickets} tickets available")

    def purchase_tickets(self, hour, num_tickets):
        # Check if tickets are available
        if self.available_tickets[hour] >= num_tickets:
            # Calculate the total price
            ticket_price = 25
            total_price = num_tickets * ticket_price

            # Apply group discount if applicable
            if num_tickets >= 10:
                free_tickets = num_tickets // 10
                total_price -= free_tickets * ticket_price

            # Update data structures
            self.available_tickets[hour] -= num_tickets
            self.total_passengers[hour] += num_tickets
            self.total_money[hour] += total_price

            print(f"Tickets purchased successfully for Train {hour}. Total price: ${total_price}")
        else:
            print(f"Error: Not enough tickets available for Train {hour}.")

    def end_of_day_summary(self):
        # Display the summary for each train journey
        for hour in ["09:00", "11:00", "13:00", "15:00"]:
            print(f"\nTrain {hour} Summary")
            print(f"Passengers: {self.total_passengers[hour]}")
            print(f"Total money taken: ${self.total_money[hour]}")

        # Calculate and display the total for the day
        total_passengers_day = sum(self.total_passengers.values())
        total_money_day = sum(self.total_money.values())

        print("\nOverall Summary for the Day")
        print(f"Total passengers for the day: {total_passengers_day}")
        print(f"Total money taken for the day: ${total_money_day}")

        # Find and display the train journey with the most passengers
        max_passengers_hour = max(self.total_passengers, key=self.total_passengers.get)
        print(f"Train journey with the most passengers: {max_passengers_hour}")

# Task 1 - Start of the day
railway = MountainRailway()
railway.display_screen()

# Task 2 - Purchasing tickets (example: purchasing 5 tickets for 09:00 train)
railway.purchase_tickets("11:00", 9)

# Display the updated screen
railway.display_screen()

# Task 3 - End of the day
railway.end_of_day_summary()
