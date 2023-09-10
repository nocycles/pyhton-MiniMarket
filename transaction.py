from tabulate import tabulate

class Transaction:
    def __init__(self, cust_name,  item_name, item_qty, item_price):
        self.item_name = str(item_name)
        self.item_qty = int(item_qty)
        self.item_price = int(item_price)
        self.cust_name = str(cust_name)
        total_price = self.item_qty*self.item_price
        self.detail_item = [[self.item_name.title(), self.item_qty, total_price]]

    def add_item(self, confirmation, item_name, item_qty, item_price):
        """
        Function for add new item into the list of shopping basket

        Parameters
        ----------
        confirmation: string
            a confirmation to add another item or not
        
        item_name: string
            item name to be added into the basket

        item_qty: integer
            item quantity of the new item to be added

        item_price: integer
            price of the new item to be added, price of per item

        Returns
        -------
        detail_item: list
            list of all items in the shopping basket
        """
        confirmation = str(confirmation.lower())
        if confirmation == "y":
            item_name=str(item_name)
            item_qty=int(item_qty)
            item_price=int(item_price)
            total_price=item_qty*item_price
            new_item=[item_name.title(),item_qty,total_price]
            self.detail_item.append(new_item)
            return self.detail_item
        elif confirmation == "n":
            return self.detail_item
        else:
            raise ValueError("Give the correct information")
    
    def update_item_name(self, confirmation, obj_update, item_name):
        """
        Function for updating item name from the shopping list

        Parameters
        ----------
        confirmation: string
            a confirmation to update item name or not
        
        obj_update: integer
            selecting which item to be updated for its name, index start from 1 not 0
        
        item_name: string
            input the new item name for the selected item in the list

        Returns
        -------
        detail_item: list
            list of all items in the shopping basket that have been updated on selected item
        """
        confirmation = str(confirmation.lower())
        obj_update = int(obj_update)
        if confirmation =="y":
            if 1 <= obj_update <= len(self.detail_item):
                item_name = str(item_name)
                self.detail_item[obj_update-1][0] = item_name.title()  
                return self.detail_item
            else:
                raise ValueError("Item not in your order list, please re-check your order list")
        elif confirmation == "n":
            return self.detail_item
        else:
            raise ValueError("Invalid input suggestion, please refer to the instruction!")
    
    def update_item_qty(self, confirmation, obj_update, item_qty):
        """
        Function for updating item quantity from the shopping list

        Parameters
        ----------
        confirmation: string
            a confirmation to update quantity price or not
        
        obj_update: integer
            selecting which item to be updated for its quantity, index start from 1 not 0
        
        item_qty: integer
            input the new item quantity for the selected item in the list

        Returns
        -------
        detail_item: list
            list of all items in the shopping basket that have been updated on selected item
        """
        confirmation = str(confirmation.lower())
        obj_update = int(obj_update)
        if confirmation =="y":
            if 1 <= obj_update <= len(self.detail_item):
                item_qty = str(item_qty.lower())
                self.detail_item[obj_update-1][1] = item_qty
                total_price = item_qty * self.item_price
                self.detail_item[obj_update-1][2] = total_price
                return self.detail_item
            else:
                raise ValueError("Item not in your order list, please re-check your order list")
        elif confirmation == "n":
            return self.detail_item
        else:
            raise ValueError("Invalid input suggestion, please refer to the instruction!")
    
    def update_item_price(self, confirmation, obj_update, item_price):
        """
        Function for updating item price from the shopping list

        Parameters
        ----------
        confirmation: string
            a confirmation to update item price or not
        
        obj_update: integer
            selecting which item to be updated for its price, index start from 1 not 0
        
        item_price: integer
            input the new item price for the selected item in the list

        Returns
        -------
        detail_item: list
            list of all items in the shopping basket that have been updated on selected item
        """
        confirmation = str(confirmation.lower())
        obj_update = int(obj_update)
        if confirmation =="y":
            if 1 <= obj_update <= len(self.detail_item):
                item_price = str(item_price.lower())
                total_price = self.item_qty * item_price
                self.detail_item[obj_update-1][2] = total_price
                return self.detail_item
            else:
                raise ValueError("Item not in your order list, please re-check your order list")
        elif confirmation == "n":
            return self.detail_item
        else:
            raise ValueError("Invalid input suggestion, please refer to the instruction!")
    
    def delete_item(self, confirmation, obj_delete):
        """
        Function to delete item from the shopping list

        Parameters
        ----------
        confirmation: string
            confirmation to delete item from the shopping list or not
        
        obj_delete: integer
            selecting which item to be deleted from the shopping list, index start from 1 not 0

        Returns
        -------
        detail_item: list
            list of all items in the shopping basket that have been updated after delete item
        """
        confirmation = str(confirmation.lower())
        obj_delete = int(obj_delete)
        if confirmation == "y":
            if 1 <= obj_delete <= len(self.detail_item):
                self.detail_item.pop(obj_delete-1)
                return self.detail_item
            else:
                raise ValueError("Item not in your order list, please re-check your order list")
        elif confirmation == "n":
            return self.detail_item
        else:
            raise ValueError("Invalid input suggestion, please refer to the instruction!")
    
    def reset_transaction(self, confirmation):
        """
        Function to reset all of the item 

        Parameters
        ----------
        confirmation: string
            confirmation to reset all item in the shopping list or not
        
        Returns
        -------
        detail_item: list
            an empty list after reset all of the items in the shopping list
        """
        confirmation = str(confirmation.lower())
        if confirmation == "y":
            self.detail_item.clear()
            return self.detail_item
        elif confirmation == "n":
            return self.detail_item
        else:
            raise ValueError("Invalid input suggestion, please refer to the instruction!")

    def check_order(self):
        """
        Function to return all of the items that have been added into the shopping list
        """
        headers = ["Item Name", "Item Quantity", "Item Price", "Total Item Price"]
        table=[]
        for item in self.detail_item:
            name, qty, total_price = item
            price= total_price/qty
            table.append([name,qty, price, total_price])

        if len(self.detail_item) == 1:
            table = [table[0]]
        else:
            table
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

    def total_price(self):
        """
        Function to see the total amount of transaction been made 
        if tranaction is above IDR 200_000 will be discounted by 5%,
        if above IDR 300_000 will be discounted by 8%,
        and if above IDR 500_000 will be discounted by 10%
        """
        total_trx = []
        for i in range(len(self.detail_item)):
            price = self.detail_item[i][2]
            total_trx.append(price)
        total = sum(total_trx)
        if total >= 200_000:
            total_amount = total - (total * 0.05)
            msg = print(f"Total amount of transactions to be paid are Rp{total_amount}")
            return msg
        elif total >= 300_000:
            total_amount = total - (total * 0.08)
            msg = print(f"Total amount of transactions to be paid are Rp{total_amount}")
            return msg
        elif total >= 500_000:
            total_amount = total - (total * 0.1)
            msg = print(f"Total amount of transactions to be paid are Rp{total_amount}")
            return msg
        else:
            msg = print(f"Total amount of transactions to be paid are Rp{total}")
            return msg