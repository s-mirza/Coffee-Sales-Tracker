price_9 = 1.75
price_12 = 1.90
price_15 = 2.00
gallon_to_fl = 128

size_9 = 0
size_12 = 0
size_15 = 0
total_sales = 0.0

def show_menu():
    print("Main Menu:")
    print("   1. Purchase A Cup of Coffee")
    print("   2. Show  Store Statistics")
    print("   3. Exit Program")
    choice = int(input("Enter your choice: "))
    while choice<1 or choice>3:
        choice = int(input("Incorrect Choice. Enter again: "))
    return choice


def purchase_coffee():
    while True:
        print("")
        print("What size are you purchasing today?")
        print("1. Small (9 fl oz): $1.75")
        print("2. Medium (12 fl oz): $1.90")
        print("3. Large (15 fl oz): $2.00")
        size_choice = int(input("Enter your choice: "))
        while size_choice<1 or size_choice>3:
            size_choice = int(input("Incorrect Choice. Enter again: "))
        if 1 <= size_choice <= 3:
            if size_choice == 1:
                size = 9
                price = price_9
            elif size_choice == 2:
                size = 12
                price = price_12
            else:
                size = 15
                price = price_15
        print("")
        print("")
        return size_choice, price
            
            
def show_stats(size_9, size_12, size_15, total_sales):
    gallons_sold = ((size_9 * 9)+ (size_12 * 12) + (size_15 * 15)) / gallon_to_fl
    total_profits = total_sales
    print("")
    print("Cups sold so far:")
    print(f"     9 oz: {size_9}")
    print(f"    12 oz: {size_12}")
    print(f"    15 oz: {size_15}")
    print("")
    print(f"Gallons Sold: {gallons_sold:.2f}")
    print(f"Total Profits Made: ${total_profits:.2f}")
    print("")
    print("")


def main():
    size_9 = 0
    size_12 = 0
    size_15 = 0
    total_sales = 0.0
    while True:
        choice = show_menu()
        if choice == 1:
            size_choice, price = purchase_coffee()
            if size_choice == 1:
                size_9 = size_9 + 1
            elif size_choice == 2:
                size_12 = size_12 + 1
            else:
                size_15 = size_15 + 1
            total_sales = total_sales + price
        elif choice == 2:
            show_stats(size_9, size_12, size_15, total_sales)
        elif choice == 3:
            break

if __name__ == "__main__":
    main()