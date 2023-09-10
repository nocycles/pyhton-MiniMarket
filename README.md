# Python Project: Mini Market System for Transactions

### A. Requirements / Objectives
This program is called as Mini Market System, where it can be used as a simple transaction while in a mini market. This program being created to solve the transaction process in a mini market, from adding items into basket, update items in the basket, remove item(s) in the basket, until calculating the total price of all items in the basket.

The program initially need a field of cust_name for customer name while shopping, item_name for first item added into the basket, item_qty for the quantity of the first item added, and item_price for the price of per item quantity.

<img src="img_start_menu.png" width="1000"/>

### B. Flowchart of the Program
#### B.1. First Step
To start the program, we need to run the main.py as our main program, while the function needed in main.py imported from the class in transaction.py

In order to initialize the program, we need the input value of cust_name (customer name), item_name, item_qty (item quantity), and item_price.

<img src="img_first_input.png" width="1000"/>

#### B.2. Add more item
In the start menu of the program after all values have been inputted, there will be menu number 1 (one), while selecting the menu will use typing method with "1".

After the add item menu have been selected, there will be a confirmation between y/n (yes or no), if we select yes, the program will ask the name of the item, quantity of the item, and price of per item quantity.

<img src="img_add_item.png" width="1000"/>

#### B.3. Update item name
In this menu, we can update the item name of the items that being added into the basket, in example we could update item name of our first item into the desired item's name.

After being selected, the program will ask the confirmation between y/n (yes or no) and then which item want to be updated (index started from 1 and above), and the new name want to be updated into selected item.

<img src="img_update_name.png" width="1000"/>

#### B.4. Update item quantity
In this menu, we can update the item quantity of the items that being added into the basket, in example we could update item quantity of our first item into the desired item's quantity.

After being selected, the program will ask the confirmation between y/n (yes or no) and then which item want to be updated (index started from 1 and above), and the new quantity want to be updated into selected item.

<img src="img_update_qty.png" width="1000"/>

#### B.5. Update item price
In this menu, we can update the item price of the items that being added into the basket, in example we could update item price of our first item into the desired item's price.

After being selected, the program will ask the confirmation between y/n (yes or no) and then which item want to be updated (index started from 1 and above), and the new price want to be updated into selected item.

<img src="img_update_price.png" width="1000"/>

#### B.6. Delete item
In the menu of delete item from this program allow us to delete selected item on our shopping list. After being selected, the program will ask the confirmation to delete item or not with the input of y/n (yes or no), and then it will be completely delete if we select which item want to be deleted from the list.

<img src="img_delete_item.png" width="1000"/>

#### B.7. Reset item
Reset item menu will allow us to reset all of the items in our shopping list. In order to prevent any miss selection of the menu, the program will ask the confirmation to the user if all of the items want to be reset or not with confirmation between y/n (yes or no).

<img src="img_reset_all.png" width="1000"/>

#### B.8. Check all items
On this menu, will allow us to check all of the items being added to our shopping list before. The program will visualize it into the table for easier checking.

<img src="img_check_item.png" width="1000"/>

##### B.9. Check total price
On this menu, the program will show to us how much we need to pay for the transaction have been done. Preferably this menu selected while we want to finish our transaction from the mini market.

<img src="img_total_price.png" width="1000"/>