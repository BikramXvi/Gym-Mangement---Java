from datetime import datetime
import read
import write

def display_inventory(inventory):
    """
    Shows the current inventory in a clean table.
    Prices are shown at 200% of their original value.
    """
    print("_" * 80)
    print("id \t name \t\t brand \t\t qty \t price \t origin")
    print("_" * 80)
    for key in inventory:
        print(key, end="\t")  # Print product ID
        value = inventory[key]  # Get product details
        index = 0
        for item in value:
            if index == 3:  # Price column
                doubled_price = int(item) * 2  # Selling price is double
                print(str(doubled_price), end="\t")
            else:
                print(item, end="\t")  # Show other details as-is
            index = index + 1
        print()
    print("_" * 80)

def sell(inventory):
    """
    Handles the selling process: takes customer info, lets them buy products, 
    applies buy-3-get-1-free offer, adds delivery charge if chosen, 
    updates inventory, and saves a bill.
    """
    customer_name = input("Customer name: ")
    phone_number = input("Phone number: ")
    selling_items = []
    total = 0
    delivery_charge = 0
    loop = True

    while loop:
        display_inventory(inventory)  # Show products before selection
        try:
            p_id = int(input("Enter product ID: "))
            if p_id <= 0 or p_id > len(inventory):
                print("Invalid product ID!")
                continue
        except ValueError:
            print("Invalid input for product ID!")
            continue

        try:
            p_qty = int(input("Quantity to buy: "))
        except ValueError:
            print("Invalid input for quantity!")
            continue

        stock = int(inventory[p_id][2])  # Check available stock
        free = p_qty // 3  # Buy 3 get 1 free offer
        total_qty = p_qty + free

        if p_qty <= 0 or total_qty > stock:
            print("Insufficient stock.")
            continue

        inventory[p_id][2] = str(stock - total_qty)  # Update stock
        price = int(inventory[p_id][3]) * 2  # Selling price is double
        sub_total = p_qty * price
        total += sub_total

        # Save item details for the bill
        selling_items.append((
            inventory[p_id][0], inventory[p_id][1], 
            p_qty, free, price, sub_total
        ))

        more = input("Add more items? (y/n): ")
        loop = more.lower() == "y"

    # Optional delivery charge
    if input("Delivery service (Rs.500)? (y/n): ").lower() == "y":
        delivery_charge = 500
    total += delivery_charge

    # Create and save the bill
    bill_no = read.read_bill_no() + 1
    write.write_bill_no(bill_no)
    filename = customer_name.replace(" ", "") + str(bill_no) + ".txt"

    # Bill contents
    lines = [
        "-------WeCare Wholesale--------",
        "   Kamalpokhari, Kathmandu",
        "  Bill No.: " + str(bill_no),
        "-------Tax Invoice ------",
        "Date: " + str(datetime.today()),
        "Customer: " + customer_name,
        "Phone: " + phone_number,
        "Items Purchased:"
    ]

    for item in selling_items:
        line = "Product: " + item[0] + " | Brand: " + item[1] + " | Qty: " + str(item[2]) + " + " + str(item[3]) + " free | Unit Price: " + str(item[4]) + " | Subtotal: " + str(item[5])
        lines.append(line)

    lines.append("Delivery Charge: " + str(delivery_charge))
    lines.append("Total: Rs. " + str(total))
    lines.append("Thank you! Visit Us again!!")

    for line in lines:
        print (line+"\n")
    write.write_individual_bill(filename, lines)  # Save detailed bill

    # Append to global bill log
    allbill = ["\nBILL NO: " + str(bill_no), "Customer: " + customer_name + " | Phone: " + phone_number]
    for item in selling_items:
        allbill_line = "Product: " + item[0] + " | Qty: " + str(item[2]) + " + " + str(item[3]) + " free | Subtotal: " + str(item[5])
        allbill.append(allbill_line)
    allbill.append("Total: Rs. " + str(total))
    allbill.append("-" * 40)
    write.append_to_all_bills(allbill)

    print("Selling successful. Bill saved to " + filename)
    write.write_inventory(inventory)  # Save updated stock

def restock(inventory):
    """
    Handles the restocking process: takes vendor info, adds new stock and price,
    updates inventory, and creates a purchase bill.
    """
    vendor_name = input("Vendor name: ")
    phone_number = input("Phone number: ")
    restocking_items = []
    total = 0
    loop = True

    while loop:
        display_inventory(inventory)  # Show current inventory
        try:
            p_id = int(input("Enter product ID: "))
            if p_id <= 0 or p_id > len(inventory):
                print("Invalid product ID!")
                continue
        except ValueError:
            print("Invalid input for product ID!")
            continue

        try:
            new_qty = int(input("Quantity to add: "))
            new_price = int(input("New cost price: "))
        except ValueError:
            print("Invalid input!")
            continue

        # Update stock and price
        inventory[p_id][2] = str(int(inventory[p_id][2]) + new_qty)
        inventory[p_id][3] = str(new_price)

        subtotal = new_qty * new_price
        total += subtotal

        # Save item details for the bill
        restocking_items.append((
            inventory[p_id][0], inventory[p_id][1], 
            new_qty, new_price, subtotal
        ))

        more = input("Add more items? (y/n): ")
        loop = more.lower() == "y"

    # Create and save the vendor bill
    bill_no = read.read_bill_no() + 1
    write.write_bill_no(bill_no)
    filename = vendor_name.replace(" ", "") + str(bill_no) + ".txt"

    lines = [
        "-------WeCare Wholesale--------",
        "   Kamalpokhari, Kathmandu",
        "  Bill No.: " + str(bill_no),
        "-------Tax Invoice ------",
        "Date: " + str(datetime.today()),
        "Vendor: " + vendor_name,
        "Phone: " + phone_number,
        "Items Restocked:"
    ]

    for item in restocking_items:
        line = "Product: " + item[0] + " | Brand: " + item[1] + " | Qty: " + str(item[2]) + " | Unit Price: " + str(item[3]) + " | Subtotal: " + str(item[4])
        lines.append(line)

    lines.append("Total: Rs. " + str(total))
    lines.append("Thank you! Visit Us again!!")

    for line in lines:
        print(line+"\n")
    write.write_individual_bill(filename, lines)  # Save detailed vendor bill

    # Append to global restock log
    allbill = ["\nBILL NO: " + str(bill_no), "Vendor: " + vendor_name + " | Phone: " + phone_number]
    for item in restocking_items:
        allbill_line = "Product: " + item[0] + " | Qty: " + str(item[2]) + " | Subtotal: " + str(item[4])
        allbill.append(allbill_line)
    allbill.append("Total: Rs. " + str(total))
    allbill.append("-" * 40)
    write.append_to_all_bills(allbill)

    print("Restock successful. Bill saved to " + filename)
    write.write_inventory(inventory)  # Save updated inventory
