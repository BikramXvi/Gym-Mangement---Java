import read
import operations

# Load inventory data from file at the start
inventory = read.read_inventory()
loop = True  # Control flag for the main menu loop

while loop:
    print("\n1: Sell\n2: Restock\n3: Display Stock\n4: Exit")
    try:
        choice = int(input("Enter choice: "))  # Get user input as a number

        if choice == 1:
            operations.sell(inventory)  # Call sell function
        elif choice == 2:
            operations.restock(inventory)  # Call restock function
        elif choice == 3:
            operations.display_inventory(inventory)  # Show current stock
        elif choice == 4:
            print("Thank you! Visit us again!")  # Exit message
            loop = False  # Stop the loop
        else:
            print("Invalid choice (1-4 only)")  # If number is outside range
    except ValueError:
        print("Invalid input! Enter a number")  # If user enters text or invalid value
