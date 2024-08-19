# Inventry Management System
products={}
subproduct={}
# Fuctions
# Add Item
def addProduct():
    global subproduct
    subproduct={}
    item_name=[]
    print("Enter Item Details:")
    print("*********************")
    
    productname=input("Enter the product name: ")
    item_qty=[]
    productqty=int(input("Enter the quatity recieved: "))
    item_price=[]
    productprice=int(input("Enter the price: "))
    item_name.append(productname)
    item_qty.append(productqty)
    item_price.append(productprice)
    subproduct["Item Name"]=item_name
    subproduct["Quantity"]=item_qty
    subproduct["Price"]=item_price
    products[productname]=subproduct
# View Item
def viewItem():
    print(subproduct)

# updation
def updateItem():
    updateItemName=input('Enter the Item Name Do You Want Delete: ')
    data_type_to_update=input('Enter the type of Data to update: Item Name\nItem Qty\nItem Price')
    data_to_update=input('Enter the Data to update: ')
    if updateItemName in products:
        products[updateItemName].update({data_type_to_update:data_to_update})
        print("Item is updated successfully")
    else:
            print("This contact not available")

# Delete Item
def deleteItem():
    item_delete=input("Enter the item namet do you want to delete")
    if item_delete in products:
        del products[item_delete]
        print("Item is deleted successfully")

    else:
            print("This contact not available")

# Display Stock
def displayStock():    
    print(products)





while True:
    print("REAL TRACK INVENTORY MANAGEMENT SYSTEM")
    print("**************************************")
    print("MENU")
    print("1. Add Product\n2. View Item\n3. Update Item\n4. Delete Item\n5. Display Stock")
    print("***********************")
    print("")

    option=int(input("Select an Option: "))


    if option==1:
        addProduct()
    elif option==2:
        viewItem()
    elif option==3:
         updateItem()
    elif option==4:
        deleteItem()
    elif option==5:
        displayStock()
    else:
         print("Enter a valid Option")

    
    