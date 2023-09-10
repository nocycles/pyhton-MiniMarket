from transaction import Transaction
    
print("Welcome to the Mini Market")
msg = "Before selecting your menu, please enter your name and your item"
print(msg)
print("-"*len(msg))
cust_name = input("Enter your name here: ")
item_name = input("Enter item name here: ")
item_qty = input("Enter the quantity of your item here: ")
item_price = input("Enter the price of your item here (@per item): ")
shopping=Transaction(cust_name, item_name, item_qty, item_price)

while True:
    print("-"*30)
    print(f"Welcome {cust_name.title()}, List of shopping menu:")
    print("-"*30)
    print("[1] Add more item")
    print("[2] Update item name")
    print("[3] Update item quantity")
    print("[4] Update item price")
    print("[5] Delete item on your shopping list")
    print("[6] Reset all of your items in your shopping list")
    print("[7] Check all your order / items in your shopping list")
    print("[8] Check all of your amount of transactions")
    print("[9] Exit")
    print("-"*30)
    selection=int(input("Select the menu in here: "))

    if selection == 1: #Function add_item
        confirmation = input("Do you want to add more items <y/n>: ")
        item_name = input("What item do you want to add?: ")
        item_qty = input("How many items do you want to add?: ")
        item_price = input("How much the item price?: ")
        shopping.add_item(confirmation, item_name, item_qty, item_price)
    elif selection == 2: #Function update_item_name
        confirmation = input("Do you want to update your item? <y/n>: ")
        obj_update = input("Which one do you want to update?: ")
        item_name = input("Update the item name: ")
        shopping.update_item_name(confirmation.lower(), obj_update, item_name.title())
    elif selection == 3: #Function update_item_qty
        confirmation = input("Do you want to update your item? <y/n>: ")
        obj_update = input("Which one do you want to update?: ")
        item_qty = input("Update the item quantity: ")
        shopping.update_item_qty(confirmation.lower(), obj_update, item_qty)
    elif selection == 4: #Function update_item_price
        confirmation = input("Do you want to update your item? <y/n>: ")
        obj_update = input("Which one do you want to update?: ")
        item_price = input("Update the item quantity: ")
        shopping.update_item_price(confirmation.lower(), obj_update, item_price)
    elif selection == 5: #Function delete_item
        confirmation = input("Do you want to delete your item? <y/n>: ")
        obj_delete = input("Which one do you want to delete?: ")
        shopping.delete_item(confirmation.lower(),obj_delete)
    elif selection == 6: #Function reset_transaction
        confirmation = input("Do you want to delete your item? <y/n>: ")
        shopping.reset_transaction(confirmation.lower())
    elif selection == 7: #Function check_order
        shopping.check_order()
    elif selection == 8: #Function total_price
        shopping.total_price()
    elif selection == 9: #Exit the program
        print("Thankyou for shopping!")
        break
    else:
        print("Invalid selection, please re-input the menu selection")
        raise ValueError("Invalid menu selection")