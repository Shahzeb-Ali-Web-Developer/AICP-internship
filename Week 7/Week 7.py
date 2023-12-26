class Charity:
    def __init__(self, name):
        self.name = name
        self.total_donation = 0

# TASK 1
def setup_donation_system():
    charities = [Charity(input(f"Enter the name of charity {i + 1}: ")) for i in range(3)]

    print("\nCharities:")
    for i, charity in enumerate(charities):
        print(f"{i + 1}. {charity.name}")

    return charities

# TASK 2
def record_and_total_donation(charities):
    while True:
        try:
            choice = int(input("Enter the number of the chosen charity (1, 2, 3), or -1 to show totals: "))
            if choice == -1:
                show_totals(charities)
                break
            elif 1 <= choice <= 3:
                shopping_bill = float(input("Enter the value of the customer's shopping bill: "))
                donation = shopping_bill * 0.01
                charities[choice - 1].total_donation += donation
                print(f"Donation of ${donation} recorded for {charities[choice - 1].name}")
            else:
                print("Invalid choice. Please enter 1, 2, 3, or -1.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# TASK 3
def show_totals(charities):
    sorted_charities = sorted(charities, key=lambda x: x.total_donation, reverse=True)

    print("\nCharities and Totals:")
    grand_total = 0
    for charity in sorted_charities:
        print(f"{charity.name}: ${charity.total_donation}")
        grand_total += charity.total_donation

    print(f"\nGRAND TOTAL DONATED TO CHARITY: ${grand_total}")

if __name__ == "__main__":
    charities = setup_donation_system()

    while True:
        record_and_total_donation(charities)
        continue_donating = input("Do you want to record donations for another customer? (yes/no): ").lower()
        if continue_donating != 'yes':
            break
