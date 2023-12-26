from datetime import datetime, timedelta

class Boat:
    def __init__(self, boat_number):
        self.boat_number = boat_number
        self.total_money = 0
        self.total_hours = 0
        self.current_hire_start = None

    def hire_boat(self, hours):
        if not self.current_hire_start:
            self.current_hire_start = datetime.now()

        if self.current_hire_start.time() < datetime.strptime("10:00", "%H:%M").time():
            self.current_hire_start = datetime.combine(self.current_hire_start.date(), datetime.strptime("10:00", "%H:%M").time())

        if self.current_hire_start.time() > datetime.strptime("17:00", "%H:%M").time():
            print("Boat can't be hired after 17:00.")
            return

        if hours == 0.5:
            cost = 12
        elif hours == 1:
            cost = 20
        else:
            print("Invalid duration. Boat can be hired for 0.5 or 1 hour only.")
            return

        self.total_money += cost
        self.total_hours += hours
        self.current_hire_start += timedelta(hours=hours)
        print(f"Boat {self.boat_number} hired for {hours} hours. Total cost: ${cost}. Total hours: {self.total_hours}")

    def get_hours_until_available(self):
        if not self.current_hire_start or self.current_hire_start.time() >= datetime.strptime("17:00", "%H:%M").time():
            return 0
        return (datetime.combine(datetime.today(), datetime.strptime("10:00", "%H:%M").time()) - self.current_hire_start).seconds / 3600

# Task 1
def calculate_daily_profits():
    boats = [Boat(i) for i in range(1, 11)]

    for boat in boats:
        while True:
            try:
                hours = float(input(f"Enter hours for boat {boat.boat_number} (0.5 or 1): "))
                boat.hire_boat(hours)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Task 2
    available_boats = [boat for boat in boats if boat.get_hours_until_available() == 0]

    if not available_boats:
        earliest_available_time = min([boat.current_hire_start for boat in boats]).strftime("%H:%M")
        print(f"No boats available. Next available time is {earliest_available_time}")
    else:
        print(f"Number of boats available: {len(available_boats)}")

    # Task 3
    total_money_taken = sum([boat.total_money for boat in boats])
    total_hours_hired = sum([boat.total_hours for boat in boats])
    unused_boats = len([boat for boat in boats if boat.total_hours == 0])
    most_used_boat = max(boats, key=lambda x: x.total_hours)

    print(f"\nTotal Money Taken: ${total_money_taken}")
    print(f"Total Hours Hired: {total_hours_hired}")
    print(f"Number of Unused Boats: {unused_boats}")
    print(f"Most Used Boat: {most_used_boat.boat_number} with {most_used_boat.total_hours} hours")

if __name__ == "__main__":
    calculate_daily_profits()
