class Sack:
    def __init__(self, contents, weight):
        self.contents = contents
        self.weight = weight


# TASK 1
def check_single_sack():
    while True:
        try:
            contents = input("Enter the contents of the sack (C for cement, G for gravel, S for sand): ").upper()
            weight = float(input("Enter the weight of the sack in kilograms: "))

            if contents not in ['C', 'G', 'S']:
                print("Invalid contents. Please enter C, G, or S.")
                continue

            if (contents == 'C' and 24.9 < weight < 25.1) or \
                    ((contents == 'G' or contents == 'S') and 49.9 < weight < 50.1):
                sack = Sack(contents, weight)
                print(f"Sack accepted. Contents: {sack.contents}, Weight: {sack.weight} kg")
                return sack
            else:
                print("Sack rejected. Incorrect weight or contents.")
        except ValueError:
            print("Invalid input. Please enter a valid weight.")


# TASK 2
def check_customer_order():
    total_weight = 0
    sacks_rejected = 0

    num_cement = int(input("Enter the number of cement sacks required: "))
    num_gravel = int(input("Enter the number of gravel sacks required: "))
    num_sand = int(input("Enter the number of sand sacks required: "))

    for _ in range(num_cement):
        sack = check_single_sack()
        total_weight += sack.weight

    for _ in range(num_gravel):
        sack = check_single_sack()
        total_weight += sack.weight

    for _ in range(num_sand):
        sack = check_single_sack()
        total_weight += sack.weight

    return total_weight


# TASK 3
def calculate_order_price(total_weight, num_cement, num_gravel, num_sand):
    regular_price = num_cement * 3 + num_gravel * 2 + num_sand * 2

    num_special_packs = min(num_cement, num_sand // 2, num_gravel // 2)
    discount_price = num_special_packs * 10

    final_price = regular_price - discount_price if discount_price > 0 else regular_price

    print(f"\nRegular Price: ${regular_price}")
    if discount_price > 0:
        print(f"Discount Price Applied: ${discount_price}")
        print(f"New Price: ${final_price}")
        print(f"Amount Saved: ${discount_price}")
    else:
        print("No discount applied. Final Price: ${final_price}")


if __name__ == "__main__":
    total_weight = check_customer_order()
    print(f"\nTotal Weight of Order: {total_weight} kg")

    calculate_order_price(total_weight, 2, 4, 6)  # Example order with 2 cement, 4 gravel, and 6 sand sacks
