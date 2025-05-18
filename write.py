def write_inventory(inventory):
    file = open("inventory.txt", "w")
    for key in inventory:
        line = inventory[key][0] + "," + inventory[key][1] + "," + inventory[key][2] + "," + inventory[key][3] + "," + inventory[key][4]
        file.write(line + "\n")
    file.close()

def write_bill_no(bill_no):
    file = open("bill_no.txt", "w")
    file.write(str(bill_no))
    file.close()

def write_individual_bill(filename, content):
    file = open("invoices/" + filename, "w")
    for line in content:
        file.write(line + "\n")
    file.close()

def append_to_all_bills(lines):
    file = open("BillsStoration.txt", "a")
    for line in lines:
        file.write(line + "\n")
    file.close()