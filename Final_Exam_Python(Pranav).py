"""
Program to Manage the Products of an Enterprise with Multiple Branch, Different People uses the Program according to
their Position in a Enterprise(WareHouse Manager, Fulfillment Manager, Employee). Everyone are Limited to their own use.

WareHouse Manager has a permission to View all the Products Available in Every wareHouse of Enterprise, Also Warehouse
Manager can Add, Move, and edit the Product.

Fulfillment manager has permission View all the Product Available in every wareHouse of enterprise, Also Fulfillment
Manager can Move View the quantity of products and Order accordingly, Program also Displays and make a Order Products
List of Product whose quantity is less than 10.

Employee has a permission to view all the Products Available in every WareHouse of Enterprise and Sell a Product and
Program makes one file of Sold Products which contains the Sold Products of Every warehouse of Enterprise.

Financial Manager can also view all the Products available in every wareHouse of Enterprise and can view the Gross Profit
as well as Individual WareHouse Profit(Profit is 10% of Total Product Sold).

The Program will also Create a Order list file named (Order_List.txt), Products added in that file are are the Products that
has less than 10 Quantity left in the WareHouse, Fulfillment Manager can take care of that to order it.

According to the WareHouse is created, they have file named East_WareHouse, West_WareHouse, South_WareHouse, Sold_Product
in their device, which contains the available Products in Inventory.

Also, Every time Adding, Moving , Editing the Details of Product will Update the Data in that File, File will be
Updated Automatically whenever any action is Performed

Employee Can Sell the Product, and the data will automatically update
"""
# List for Storing data of Different Location WareHouse
East_name, East_count, East_price = [], [], []
West_name, West_count, West_price = [], [], []
South_name, South_count, South_price = [], [], []
Sold_name, Sold_count, Sold_price, Sold_WareHouse = [], [], [], []
# Function to Open and Read Files to make List
def Open_Files():
    # Open East WareHouse File
    East_WareHouse_list = open("East_WareHouse.txt", "r")
    items1 = East_WareHouse_list.readlines()
    for item in items1:                                                 # Loop to make a list of name, quantity and price in East Warehouse File
        name, count, price = (item.strip()).split(",")
        East_name.append(name)
        East_count.append(count)
        East_price.append(price)
    # Open West WareHouse File
    West_WareHouse_list = open("West_WareHouse.txt", "r")
    items2 = West_WareHouse_list.readlines()
    for item in items2:                                                 # Loop to make a list of name, quantity and price in West Warehouse File
        name, count, price = (item.strip()).split(",")
        West_name.append(name)
        West_count.append(count)
        West_price.append(price)
    # Open South WareHouse File
    South_WareHouse_list = open("South_WareHouse.txt", "r")
    items3 = South_WareHouse_list.readlines()
    for item in items3:                                                 # Loop to make a list of name, quantity and price in South Warehouse File
        name, count, price = (item.strip()).split(",")
        South_name.append(name)
        South_count.append(count)
        South_price.append(price)
    # Open Sold Product File
    Sold_Product_list = open("Sold_Products.txt", "r")
    item4 = Sold_Product_list.readlines()
    for item in item4:                                                  # Loop to make a list of name, quantity price and WareHousename in Sold Product File
        name, count, price, warehouse = (item.strip()).split(",")
        Sold_name.append(name)
        Sold_count.append(count)
        Sold_price.append(price)
        Sold_WareHouse.append(warehouse)
# Function to Write and make a Updated file, Also makes the Order list text file for placing order
def WriteFile():
    f_east = open("East_WareHouse.txt", "w")
    f_west = open("West_WareHouse.txt", "w")
    f_south = open("South_WareHouse.txt", "w")
    f_order_list = open("Order_list.txt", "w")                                                          # File for Order List
    f_sold_items = open("Sold_Products.txt","w")                                                        # File for Sold Items
    f_order_list.write("East WareHouse:\n")
    for i in range(len(East_name)):
        f_east.write("{:},{:},{:}\n".format(East_name[i],East_count[i], East_price[i]))                 # Updates the East WareHouse File
        if float(East_count[i]) < 10:
            f_order_list.write("{:},{:},{:}\n".format(East_name[i], East_count[i], East_price[i]))      # Updates the Order Product FIle
    f_order_list.write("\n")
    f_order_list.write("West WareHouse:\n")
    for i in range(len(West_name)):
        f_west.write("{:},{:},{:}\n".format(West_name[i],West_count[i], West_price[i]))                 # Updates the West WareHouse File
        if float(West_count[i]) < 10:
            f_order_list.write("{:},{:},{:}\n".format(West_name[i],West_count[i], West_price[i]))
    f_order_list.write("\n")
    f_order_list.write("South WareHouse:\n")
    for i in range(len(South_name)):
        f_south.write("{:},{:},{:}\n".format(South_name[i],South_count[i], South_price[i]))         # Updates the South WareHouse File
        if float(South_count[i]) < 10:
            f_order_list.write("{:}, {:},{:}\n".format(South_name[i],South_count[i], South_price[i]))
    for i in range(len(Sold_name)):
        f_sold_items.write("{:},{:},{:},{:}\n".format(Sold_name[i], Sold_count[i], Sold_price[i], Sold_WareHouse[i]))   # Updates the Sold Products File

# Function to add new Items/Product
def AddItems():
    while(True):
        print("\n1. Add New Item\n2. Add Existing Item\n----------------------------------------")
        input_Add = int(input("Select your option :"))
        if input_Add == 1:                                                                          # For Adding New Items/Products
            location = ShowAllProduct_Menu()
            Add_itemname = input("Enter Item Name : ")
            Add_itemquantity = input("Enter total number of Quantity : ")
            Add_itemprice = input("Enter the price per Quantity : ")
            if location == 1:                                                                       # Add New quantity in East WareHouse
                East_name.append(Add_itemname)
                East_count.append(Add_itemquantity)
                East_price.append(str(int(Add_itemprice)*int(Add_itemquantity)))
            elif location == 2:                                                                     # Add New quantity in West WareHouse
                West_name.append(Add_itemname)
                West_count.append(Add_itemquantity)
                West_price.append(str(int(Add_itemprice)*int(Add_itemquantity)))
            elif location == 3:                                                                     # Add New quantity in South WareHouse
                South_name.append(Add_itemname)
                South_count.append(Add_itemquantity)
                South_price.append(str(int(Add_itemprice)*int(Add_itemquantity)))
        elif input_Add == 2:                                                                        # For Adding Quantity in Existing Product
            location = ShowAllProduct_Menu()
            Add_itemname = input("Enter Item Name : ")
            Add_itemquantity = input("Enter total number of Quantity : ")
            Add_itemprice = input("Enter the price per Quantity : ")
            if location == 1:                                                               # Add Quantity for Existing Product in East WareHouse
                for i in range(len(East_name)):
                    if East_name[i] == Add_itemname:
                        East_count[i] = str(float(East_count[i]) + float(Add_itemquantity))
                        East_price[i] = str(float(East_price[i]) + float(Add_itemprice) * int(Add_itemquantity))
            if location == 2:                                                               # Add Quantity for Existing Product in West WareHouse
                for i in range(len(West_name)):
                    if West_name[i] == Add_itemname:
                        West_count[i] = str(float(West_count[i]) + float(Add_itemquantity))
                        West_price[i] = str(float(West_price[i]) + float(Add_itemprice) * int(Add_itemquantity))
            if location == 3:                                                               # Add Quantity for Existing Product in South WareHouse
                for i in range(len(South_name)):
                    if South_name[i] == Add_itemname:
                        South_count[i] = str(float(South_count[i]) + float(Add_itemquantity))
                        South_price[i] = str(float(South_price[i]) + float(Add_itemprice) * int(Add_itemquantity))
        WriteFile()                                                                              # Saves the Updated Product
        input1 = input("Want to add More Items (y/n): ")
        if input1 == 'n' or input1 == 'N':
            break

# Function to move Items/ Product
def Move_Items():
    while(True):
        print("Welcome to ABC \n----------------------------------------")
        print("\t1. East to West\n\t2. East to South\n\t3. West to East\n\t4. West to South\n\t5. South to East\n\t6. South to West")
        input_move = int(input("Move From : "))
        Move_itemname = input("Enter Item Name : ")
        Move_itemquantity = input("Enter total number of Quantity : ")
        Move_itemprice = input("Enter the price per Quantity : ")
        if input_move == 1:                                                                     # For East to west
            for i in range(len(East_name)):
                if East_name[i].lower() == Move_itemname.lower():                               # checks for any input lower of upper
                    East_count[i] = str(float(East_count[i]) - float(Move_itemquantity))                            # Updates Quantity in East
                    East_price[i] = str(float(East_price[i]) - float(Move_itemprice) * float(Move_itemquantity))    # Updates the price in East
            for i in range(len(West_name)):
                if West_name[i].lower() == Move_itemname.lower():
                    West_count[i] = str(float(West_count[i]) + float(Move_itemquantity))                            # Updates Quantity in West
                    West_price[i] = str(float(West_price[i]) + float(Move_itemprice) * float(Move_itemquantity))    # Updates Price in West
                    break
                elif i == len(West_name) - 1 and (West_name[i].lower() != Move_itemname.lower):  # If the product moving is not there in West it appends it
                    West_name.append(Move_itemname)                                                                 # Appends the Name of Product
                    West_count.append(Move_itemquantity)                                                            # Appends Quantity of Product
                    West_price.append(str(float(Move_itemprice) * float(Move_itemquantity)))                        # Appends the price of Product
        if input_move == 2:                                                                     # For East to South
            for i in range(len(East_name)):
                if East_name[i].lower() == Move_itemname.lower():
                    East_count[i] = str(float(East_count[i]) - float(Move_itemquantity))                            # Updates Quantity in East
                    East_price[i] = str(float(East_price[i]) - float(Move_itemprice) * float(Move_itemquantity))    # Updates the price in East
            for i in range(len(South_name)):
                if South_name[i].lower() == Move_itemname.lower():
                    South_count[i] = str(float(South_count[i]) + float(Move_itemquantity))                          # Updates Quantity in South
                    South_price[i] = str(float(South_price[i]) + float(Move_itemprice) * float(Move_itemquantity))  # Updates the price in South
                    break
                elif i == len(South_name) - 1 and (South_name[i].lower() != Move_itemname.lower):  # If the product moving is not there in South it appends it
                    South_name.append(Move_itemname)                                                                # Appends the Name of Product
                    South_count.append(Move_itemquantity)                                                           # Appends Quantity of Product
                    South_price.append(str(float(Move_itemprice) * float(Move_itemquantity)))                       # Appends the price of Product
        if input_move == 3:                                                                     # For West to East
            for i in range(len(West_name)):
                if West_name[i].lower() == Move_itemname.lower():
                    West_count[i] = str(float(West_count[i]) - float(Move_itemquantity))                            # Updates the Quantity in West
                    West_price[i] = str(float(West_price[i]) - float(Move_itemprice) * float(Move_itemquantity))    # Updates the price in West
            for i in range(len(East_name)):
                if East_name[i].lower() == Move_itemname.lower():
                    East_count[i] = str(float(East_count[i]) + float(Move_itemquantity))                            # Updates Quantity in East
                    East_price[i] = str(float(East_price[i]) + float(Move_itemprice) * float(Move_itemquantity))    # Updates the price in East
                    break
                elif i == len(East_name) - 1 and (East_name[i].lower() != Move_itemname.lower):  # If the product moving is not there in East it appends it
                    East_name.append(Move_itemname)                                                                 # Appends the Name of Product
                    East_count.append(Move_itemquantity)                                                            # Appends Quantity of Product
                    East_price.append(str(float(Move_itemprice) * float(Move_itemquantity)))                        # Appends the price of Product
        if input_move == 4:                                                                   # For West to South
            for i in range(len(West_name)):
                if West_name[i].lower() == Move_itemname.lower():
                    West_count[i] = str(int(West_count[i]) - int(Move_itemquantity))                                # Updates the Quantity in West
                    West_price[i] = str(int(West_price[i]) - int(Move_itemprice) * int(Move_itemquantity))          # Updates the price in West
            for i in range(len(South_name)):
                if South_name[i].lower() == Move_itemname.lower():
                    South_count[i] = str(int(South_count[i]) + int(Move_itemquantity))                              # Updates the Quantity in South
                    South_price[i] = str(int(South_price[i]) + int(Move_itemprice) * int(Move_itemquantity))        # Updates the price in South
                    break
                elif i == len(South_name) - 1 and (South_name[i].lower() != Move_itemname.lower):  # If the product moving is not there in South it appends it
                    South_name.append(Move_itemname)                                                                # Appends the Name of Product
                    South_count.append(Move_itemquantity)                                                           # Appends Quantity of Product
                    South_price.append(str(int(Move_itemprice) * int(Move_itemquantity)))                           # Appends the price of Product
        if input_move == 5:                                                                 # For South to East
            for i in range(len(South_name)):
                if South_name[i].lower() == Move_itemname.lower():
                    South_count[i] = str(float(South_count[i]) - float(Move_itemquantity))                          # Updates the Quantity in South
                    South_price[i] = str(float(South_price[i]) - float(Move_itemprice) * float(Move_itemquantity))  # Updates the price in South
            for i in range(len(East_name)):
                if East_name[i].lower() == Move_itemname.lower():
                    East_count[i] = str(float(East_count[i]) + float(Move_itemquantity))                            # Updates the Quantity in East
                    East_price[i] = str(float(East_price[i]) + float(Move_itemprice) * float(Move_itemquantity))    # Updates the price in East
                    break
                elif i == len(East_name) - 1 and (East_name[i].lower() != Move_itemname.lower):  # If the product moving is not there in East it appends it
                    East_name.append(Move_itemname)                                                                 # Appends the Name of Product
                    East_count.append(Move_itemquantity)                                                            # Appends Quantity of Product
                    East_price.append(str(float(Move_itemprice) * float(Move_itemquantity)))                        # Appends the price of Product
        if input_move == 6:                                                                 # For South to West
            for i in range(len(South_name)):
                if South_name[i].lower() == Move_itemname.lower():
                    South_count[i] = str(float(South_count[i]) - float(Move_itemquantity))                          # Updates the Quantity in South
                    South_price[i] = str(float(South_price[i]) - float(Move_itemprice) * float(Move_itemquantity))  # Updates the price in south
            for i in range(len(West_name)):
                if West_name[i].lower() == Move_itemname.lower():
                    West_count[i] = str(float(West_count[i]) + float(Move_itemquantity))                            # Updates the Quantity in West
                    West_price[i] = str(float(West_price[i]) + float(Move_itemprice) * float(Move_itemquantity))    # Updates the price in West
                    break
                elif i == len(West_name) - 1 and (West_name[i].lower() != Move_itemname.lower):  # If the product moving is not there in West it appends it
                    West_name.append(Move_itemname)                                                                 # Appends the Name of Product
                    West_count.append(Move_itemquantity)                                                            # Appends Quantity of Product
                    West_price.append(str(float(Move_itemprice) * float(Move_itemquantity)))                        # Appends the price of Product
        print("Item Moved")
        inp1 = input("Want to Move another item (y/n): ")
        if inp1 == 'n' or inp1 == 'N':
            break

# Function to Print the Stock in WareHouses
def Print(l1, l2, l3, str):
    print("\nStock in " + str + " WareHouse\n------------------------------------------------------------------")
    print("Name\t\t\t\t |    Quantity\t\t\t  | Price\n------------------------------------------------------------------")
    [print("{:<20} |\t  {:<20}|\t$ {:<20}".format(*row)) for row in zip(l1, l2, l3)]                                # Prints the Table of WareHouse
    print("------------------------------------------------------------------")
    for i in range(len(l2)):                                                                                        # loop to convert the string list into float list
        l2[i] = float(l2[i])
        l3[i] = float(l3[i])
    print("Sum:\t\t\t\t |\t  {:<20}|\t$ {:<20}".format(sum(l2), sum(l3)))                                           # prints the Sum of Called wareHouse
    WriteFile()

# Function to Print the Order List if the Products are less than 10
def OrderList():
    order_input = ShowAllProduct_Menu()
    print("Order Statement :")
    if order_input == 1 or order_input == 4:                                                                        # Prints for East and All WareHouse
        print("------------------------------------------------------------------\nFor East WareHouse\n------------------------------------------------------------------")
        print("\t Name\t\t\t\t\t Quantity\t\t\t\t  Price")
        for i in range(len(East_count)):
            if float(East_count[i]) < 10:
                print("\t {:<20}\t {:<20}\t  {:<20}".format(East_name[i], East_count[i], East_price[i]))
    if order_input == 2 or order_input == 4:                                                                        # Prints for West and All WareHouse
        print("------------------------------------------------------------------\nFor West WareHouse\n------------------------------------------------------------------")
        print("\t Name\t\t\t\t\t Quantity\t\t\t\t  Price")
        for i in range(len(West_count)):
            if float(West_count[i]) < 10:
                print("\t {:<20}\t {:<20}\t  {:<20}".format(West_name[i], West_count[i], West_price[i]))
    if order_input == 3 or order_input == 4:                                                                        # Prints for South and All WareHouse
        print("------------------------------------------------------------------\nFor South WareHouse\n------------------------------------------------------------------")
        print("\t Name\t\t\t\t\t Quantity\t\t\t\t  Price")
        for i in range(len(South_count)):
            if float(South_count[i]) < 10:
                print("\t {:<20}\t {:<20}\t  {:<20}".format(South_name[i], South_count[i], South_price[i]))

# FUnction to Display the menu after selecting their Position
def Menu(user):
    print("\nWelcome to ABC Group\n----------------------------------------\n\t1. Show All Products")
    if user == 1:                                                                                                   # Menu for WareHouse Manager
        print("\t2. Add Products\n\t3. Move Product\n\t4. Edit Price of product\n\t5. Exit")
    elif user == 2:                                                                                                 # Menu for Fulfillment Manager
        print("\t2. Add Products\n\t3. Order List\n\t4. Exit")
    elif user == 4:                                                                                                 # Menu for Employee
        print("\t2. Mark the Product as Sold\n\t3. Exit")
        #print("\t3. Exit")
    elif user == 3:                                                                                                 # Menu for Financial Manager
        print("\t2. Profit by WareHouse\n\t3. Gross Profit by Enterprise\n\t4. Exit")
    print("----------------------------------------")
    return int(input("What would you like to do? :"))                                                               # Returns the task chosed by user

# Function to Print the table of Available Products
def Call_Print():
    input_show = ShowAllProduct_Menu()
    if input_show == 1:
        Print(East_name, East_count, East_price, "East")
    elif input_show == 2:
        Print(West_name, West_count, West_price, "West")
    elif input_show == 3:
        Print(South_name, South_count, South_price, "South")
    else:
        Print(East_name, East_count, East_price, "East")
        Print(West_name, West_count, West_price, "West")
        Print(South_name, South_count, South_price, "South")

# Function for selection of WareHouse
def ShowAllProduct_Menu():
    print("\nSelect a WareHouse\n----------------------------------------")
    print("\t1. East WareHouse :\n\t2. West WareHouse :\n\t3. South WareHouse :\n\t4. All WareHouse: ")
    return int(input("Which Warehouse you would like to select : "))

# Function to Display the Admin Menu
def Admin_Menu():
    print("****************************************")
    print("Welcome to ABC Enterprise: ")
    print("****************************************")
    print("\t1. Warehouse Manager\n\t2. Fulfillment Manager\n\t3. Financial Manager\n\t4. Employee")
    return int(input("Select your Position :"))                                                                     # Returns the Position of User

Sold = {}
def Print_Sold():                                                                                                   # Function to print the Recent Sold Products
    print("\nTotal Items Sold Recently:\n----------------------------------------")
    print("Name\t\t\tQuantity")
    for i in Sold:
        print("{:<20}{:<20}".format(Sold[i], i))
    WriteFile()

# Function to Sold the Product and update in file
def Sold_Items():
    while(True):
        print("\nSelect a WareHouse\n----------------------------------------")
        print("\t1. East WareHouse :\n\t2. West WareHouse :\n\t3. South WareHouse :")
        WareHouse = int(input("Select a WareHouse : "))
        product_sold = str(input("Name of the Product that is sold : "))
        if WareHouse == 1:                                                              # For East WareHouse
            for i in range(len(East_name)):
                if product_sold.lower() == East_name[i].lower():                                                    # converts in lower case and check condition
                    quantity_sold = int(input("Enter the number of Quantity Sold : "))
                    if float(East_count[i]) < quantity_sold:                                                        # If sufficient Quantity of Product is not available
                        print("East WareHouse does not have that much quantity which can be sold\nTry Again")       # Shows Error
                        break
                    elif float(East_count[i]) > quantity_sold:                                                      # if sufficient Quantity of Product is available
                        East_price[i] = str(float(East_price[i]) - (float(East_price[i]) / float(East_count[i]) * quantity_sold))   # Updates East Price
                        East_count[i] = str(float(East_count[i]) - quantity_sold)                                    # Updates East Quantity
                        Sold[quantity_sold] = East_name[i]                                                           # Appends in Dictionary
                        for j in range(len(Sold_name)):
                            if Sold_name[j].lower() == product_sold.lower() and Sold_WareHouse[j] == 'East':        # If Product is Available in Sold File
                                Sold_count[j] = str(float(Sold_count[j])+quantity_sold)                             # Updates Sold Quantity
                                Sold_price[j] = str((float(East_price[i])/float(East_count[i]))*float(Sold_count[j])) # Updtes Sold Price
                                break
                            # If Product is not available in Sold Product File
                            elif Sold_name[j] != product_sold and Sold_WareHouse[j] != "East" and Sold_WareHouse[j] != "West" and Sold_WareHouse[j] != "South":
                                Sold_name.append(product_sold)                                                      # Appends the Name of Product in Sold Product                                                   #
                                Sold_count.append(quantity_sold)                                                    # Appends Sold Quantity in Sold Products
                                Sold_price.append(str(float(East_price[i])/float(East_count[i])*quantity_sold))     # Appends the Price in Sold product
                                Sold_WareHouse.append("East")                                                       # Appends East warehouse in Sold Quantity
        if WareHouse == 2:                                                      # For West WareHouse
            for i in range(len(West_name)):
                if product_sold.lower() == West_name[i].lower():                                                    # converts in lower case and check condition
                    quantity_sold = int(input("Enter the number of Quantity Sold : "))
                    if float(West_count[i]) < quantity_sold:                                                        # If sufficient Quantity of Product is not available
                        print("East WareHouse does not have that much quantity which can be sold\nTry Again")       # Shows error
                        break
                    elif float(West_count[i]) > quantity_sold:                                                      # if sufficient Quantity of Product is available
                        West_price[i] = str(float(West_price[i]) - (float(West_price[i]) / float(West_count[i]) * quantity_sold))   # Updates West Price
                        West_count[i] = str(float(West_count[i]) - quantity_sold)                                   # Updates West Quantity
                        Sold[quantity_sold] = West_name[i]                                                          # Updates in Dictionary
                        for j in range(len(Sold_name)):
                            if Sold_name[j].lower() == product_sold.lower() and Sold_WareHouse[j] == "West":        # If Product is Available in Sold File
                                Sold_count[j] = str(float(Sold_count[j])+quantity_sold)                             # Updates Sold Quantity
                                Sold_price[j] = str((float(West_price[i])/float(West_count[i]))*float(Sold_count[j]))   # Updates the Sold Price
                            # If Product is not available in Sold Product File
                            elif Sold_name[j] != product_sold and Sold_WareHouse[j] != "East" and Sold_WareHouse[j] != "West" and Sold_WareHouse[j] != "South":
                                Sold_name.append(product_sold)                                                      # Appends the Name of Product in Sold Product
                                Sold_count.append(quantity_sold)                                                    # Appends Sold Quantity in Sold Products
                                Sold_price.append(str(float(West_price[i])/float(West_count[i])*quantity_sold))     # Appends the Price in Sold product
                                Sold_WareHouse.append("West")                                                       # Appends West warehouse in Sold Quantity
                                break
        if WareHouse == 3:                                                      # For South WareHouse
            for i in range(len(South_name)):
                if product_sold.lower() == South_name[i].lower():                                                   # converts in lower case and check condition
                    quantity_sold = int(input("Enter the number of Quantity Sold : "))
                    if float(South_count[i]) < quantity_sold:                                                       # If sufficient Quantity of Product is not available
                        print("East WareHouse does not have that much quantity which can be sold\nTry Again")       # Shows Error
                        break
                    elif float(South_count[i]) > quantity_sold:                                                     # if sufficient Quantity of Product is available
                        South_price[i] = str(float(South_price[i]) - (float(South_price[i]) / float(South_count[i]) * quantity_sold))   # Updates South Price
                        South_count[i] = str(float(South_count[i]) - quantity_sold)                                 # Updates the South Quantity
                        Sold[quantity_sold] = South_name[i]
                        for j in range(len(Sold_name)):
                            if Sold_name[j].lower() == product_sold.lower() and Sold_WareHouse[j] == "South":       # If Product is Available in Sold File
                                Sold_count[j] = str(float(Sold_count[j])+quantity_sold)                             # Updates Sold Quantity
                                Sold_price[j] = str((float(South_price[i])/float(South_count[i]))*float(Sold_count[j]))     # Updates the Sold Price
                            # If Product is not available in Sold Product File
                            elif Sold_name[j] != product_sold and Sold_WareHouse[j] != "East" and Sold_WareHouse[j] != "West" and Sold_WareHouse[j] != "South":
                                Sold_name.append(product_sold)                                                      # Appends the Name of Product in Sold Product
                                Sold_count.append(quantity_sold)                                                    # Appends Sold Quantity in Sold Products
                                Sold_price.append(str(float(South_price[i])/float(South_count[i])*quantity_sold))   # Appends the Price in Sold product
                                Sold_WareHouse.append("South")                                                      # Appends South warehouse in Sold Quantity
                                break
        WriteFile()
        sold_input = input("Want to Mark Sold to another Product (y/n): ")
        if sold_input == 'n' or sold_input == 'N':
            break

# Function to Edit the Details in Products
def Edit_Product(l1,l2,l3,str1):
    product_name = str(input("Enter a Product Name : "))
    product_price = float(input("Product New Price : "))
    if str1 == "East":                                                                                              # For East wareHouse
        for i in range(len(East_name)):
            if East_name[i].lower() == product_name.lower():
                East_price[i] = l3[i] =  product_price * float(East_count[i])                                       # Updates price in East WareHouse
    if str1 == "West":                                                                                              # For West WareHouse
        for i in range(len(West_name)):
            if West_name[i].lower() == product_name.lower():
                West_price[i] = l3[i] = product_price * float(West_count[i])                                        # Updates price in west WareHouse
    if str1 == "South":                                                                                             # For South WareHouse
        for i in range(len(South_name)):
            if South_name[i].lower() == product_name.lower():
                South_price[i] = l3[i] =  product_price * float(South_count[i])                                     # Updates price in South WareHouse
    inp1 = input("Want to View the Updated List : (y/n)")
    if inp1 == "y" or inp1 == "y":
        Print(l1, l2, l3, str1)                                                                                     # prints the Recent Sold Products

# Function for task that can be perfom by Finance Manager
def Finance_Print(inp):
    l_east, l_west, l_south = [], [], []
    for i in range(len(Sold_WareHouse)):
        Sold_price[i] = float(Sold_price[i])
        if Sold_WareHouse[i] == "East":
            l_east.append(float(Sold_price[i]))                                                                     # Converts string values into float and adds to l_east
        if Sold_WareHouse[i] == "West":
            l_west.append(float(Sold_price[i]))                                                                     # Converts string values into float and adds to l_west
        if Sold_WareHouse[i] == "South":
            l_south.append(float(Sold_price[i]))                                                                    # Converts string values into float and adds to l_south
    if inp == 2 :                                                                                     # To print Profit of Individual WareHouse
        print("\t 1. East WareHouse\n\t 2. West WareHouse\n\t 3. South WareHouse")
        select = int(input("Select a WareHouse Which You Want Gross Profit : "))
        if select == 1 :                                                                                             # Prints the Profit of East Warehouse
            print("\nName\t\t\t\tQuantity Sold\t\tPrice\n------------------------------------------------")
            for i in range(len(Sold_name)):                                               # loop to print the individual Profit of Product in East WareHouse
                if Sold_WareHouse[i] == "East":
                    print("{:<20}{:<20}{:<10}".format(Sold_name[i], Sold_count[i], float(Sold_price[i])*.1))
            print("\nSum of Profit on East WareHouse is : ${:<20}".format(sum(l_east)*.1))
        elif select == 2:                                                                                           # Prints the Profit of West Warehouse
            print("\nName\t\t\t\tQuantity Sold\t\tPrice\n------------------------------------------------")
            for i in range(len(Sold_name)):                                               # loop to print the individual Profit of Product in East WareHouse
                if Sold_WareHouse[i] == "West":
                    print("{:<20}{:<20}{:<10}".format(Sold_name[i], Sold_count[i], float(Sold_price[i]) * .1))
            print("\nSum of Profit on West WareHouse is : ${:<20}".format(sum(l_west) * .1))
        elif select == 3:                                                                                           # Prints the Profit of Sast Warehouse
            print("\nName\t\t\t\tQuantity Sold\t\tPrice\n------------------------------------------------")
            for i in range(len(Sold_name)):                                               # loop to print the individual Profit of Product in East WareHouse
                if Sold_WareHouse[i] == "South":
                    print("{:<20}{:<20}{:<10}".format(Sold_name[i], Sold_count[i], float(Sold_price[i]) * .1))
            print("\nSum of Profit on South WareHouse is : ${:<20}".format(sum(l_south) * .1))
    if inp == 3:                                                                                                    # Prints the Gross Profit of Enterprise
        print("\nGross Profit of All WareHouse is : ${:<20}".format(sum(Sold_price) * .1))
        print("To View Profit in Detail, Select Profit by WareHouse Option")
    if inp == 4:                                                                                                    # Quits the Program
        exit()

# Function for taks that can be perfom by WareHouse Manager
def WareHouse_Manager():
    while (True):
        input_menu = Menu(input_admin)
        if input_menu == 1:                                                                          # To Print the table of Product Available in WareHouse
            Call_Print()
        elif input_menu == 2:                                                                        # Function call to Add New Product and Quantity in Existing Products
            AddItems()
            WriteFile()
            print("\nProduct Added to your WareHouse")
        elif input_menu == 3:                                                                       # Function call to move the Item/Product to Different wareHouse
            Move_Items()
            WriteFile()
            print("\nProduct Moved to Your WareHouse")
        elif input_menu == 4:                                                                       # Function call to Edit the Details in Product
            print("\nSelect a WareHouse\n----------------------------------------")
            print("\t1. East WareHouse :\n\t2. West WareHouse :\n\t3. South WareHouse :")
            inp = int(input("Select a wareHouse where you want to edit the price of item : "))
            if inp == 1:                                                                                            # For East WareHouse
                Edit_Product(East_name, East_count, East_price, "East")
            elif inp == 2:                                                                                          # For West wareHouse
                Edit_Product(West_name, West_count, West_price, "West")
            elif inp == 3:                                                                                          # For South wareHouse
                Edit_Product(South_name, South_count, South_price, "South")
        elif input_menu == 5:                                                                                       # Quits the Program
            exit()

# Function for taks that can be perfom by Fulfillment Manager
def FulFillment_Manager():
    while (True):
        input_menu = Menu(input_admin)                                                                              # Function call for Particular task to perform by Position
        if input_menu == 1:
            Call_Print()                                                                                            # Function call to print the Table of Available Products in WareHouse
        elif input_menu == 2:
            print("Add Items")
            AddItems()                                                                                              # Function call to Add Items/Products
        elif input_menu == 3:
            OrderList()                                                                                             # Function call to Print the Order List
            WriteFile()                                                                                             # Saves the Updated File after changes
            print("\nOrder list Text file Created in your Device Which you can Print")
        elif input_menu == 4:                                                                                       # Quits the Program
            exit()

# Function for taks that can be perfom by Employee
def Employee():
    while(True):
        input_menu = Menu(input_admin)                                                                              # Function call for Particular task to perform by Position
        if input_menu == 1:
            Call_Print()                                                                                            # Function call to print the Table of Available Products in WareHouse
        elif input_menu == 2:
            Sold_Items()                                                                                            # Function call to Sold the Product
            emp_input = input("Want to Print the Statement of Sold Items(y/n) : ")
            if emp_input == 'n' or emp_input == 'N':
                break
            Print_Sold()                                                                                                # Prints the recent sold products
            WriteFile()                                                                                                 # Save a File
        elif input_menu == 3:
            exit()

# Function for taks that can be perfom by Finance Manager
def Finance_Manager():
    while (True):
        input_menu = Menu(input_admin)                                                                              # Function call for Particular task to perform by Position
        if input_menu == 1:
            Call_Print()                                                                                            # Function call to print the Table of Available Products in WareHouse
        elif input_menu == 2 or 3:                                                                                  # Function call to Print the Profits
            Finance_Print(input_menu)

if __name__ == "__main__":
    Open_Files()                                                                            # Opens the Files
    input_admin = Admin_Menu()                                                              # Function call to Select the Position
    if input_admin == 1:
        WareHouse_Manager()                                                                 # Function call for WareHouse Manager
    elif input_admin == 2:
        FulFillment_Manager()                                                               # Function call for Fulfillment Manager
    elif input_admin == 3:
        Finance_Manager()                                                                   # Function call for Finance Manager
    elif input_admin == 4:
        Employee()                                                                          # Quits the Program