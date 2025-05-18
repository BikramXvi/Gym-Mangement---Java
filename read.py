def read_inventory():
    """f
    Reads all inventory data from 'inventory.txt' and stores it in a dictionary.
    Each product gets a unique ID starting from 1.
    Returns the inventory dictionary.
    """

    inventory = {}  # Create an empty dictionary to store the inventory

    file = open("inventory.txt", "r")  # Open the inventory file for reading
    data = file.readlines()           # Read all lines from the file
    file.close()                      # Always close the file after reading
    
    p_id = 1  # We'll use this as the product ID, starting from 1
    
    for line in data:
        line = line.replace("\n", "").split(",")  # Clean the line and split by commas
        inventory[p_id] = line  # Store the product details in the dictionary
        p_id = p_id + 1  # Move to the next product ID
    return inventory  # Return the full inventory dictionary



def read_bill_no():
    """
    Reads the last used bill number from 'bill_no.txt'.
    Returns the bill number as an integer.
    """

    file = open("bill_no.txt", "r")  # Open the file that has the bill number
    bill_no = int(file.read())       # Read and convert to integer
    file.close()                     # Close the file

    return bill_no  # Return the bill number
