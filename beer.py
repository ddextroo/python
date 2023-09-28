#beer beer distributorship

import random

beer = [
    [1, "Red Horse"],
    [2, "San Mig Light"],
    [3, "San Miguel Pilsen"],
    [4, "Colt 45"],
    [5, "Gold Eagle"],
    [6, "Heineken"],
    [7, "Tiger Crystan"],
]

storage = []
for beer_brands in beer:
    random_values = random.randint(1000, 9999)
    storage.append(
        [beer_brands[0], random_values, random_values]
    )  # brand_id, stocks_before_sales, stocks_after_sales

def get_case_inventory():
    print("Inventory before the sales")
    for brand in storage:
        brand_id, brand_items, _ = brand
        print(
            f"Brand ID: {brand_id}\nBrand Name: {beer[brand_id-1][1]}\nBrand Items: {brand_items}\n\n"
        )

def weekly_sales():
    print("Sales and purchase records each brand(negative for sales)")
    brand_id = int(input("Enter brand id: "))

    if not brand_id in range(1, 8):
        print("Invalid brand id")
        
    quantity = int(input("Enter quantity: "))
    
    storage[brand_id-1][2] += quantity


def display_final_inventory():
    print("Inventory after the sales")
    for brand in storage:
        brand_id, _, brand_items = brand
        print(
            f"Brand ID: {brand_id}\nBrand Name: {beer[brand_id-1][1]}\nBrand Items: {brand_items}\n\n"
        )

if __name__ == "__main__":
    print("Beer Inventory System")
    while True:
        print(
            """Select choices:
        (a). Get the case inventory for each brand for the start of the week.
        (b). Process all weekly sales and puchase records for each brand.
        (c). Display out the final inventory
        (q). Exit"""
        )
        choice = input("Select your choice: ").lower()

        if choice == "a":
            get_case_inventory()
        elif choice == "b":
            weekly_sales()
        elif choice == "c":
            display_final_inventory()
        elif choice == "q":
            print("See you around")
            break
        else:
            print("Invalid choice")
