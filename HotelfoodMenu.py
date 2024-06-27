# Hotel Cart Mini Project 

print("Welcome to Hotel Dinner Hut!...")
print("Menu")
print("*")
print("1.Bread = ₹30\n2.Dosa = ₹40\n3.Gravy = ₹60\n4.Rice = ₹100\n5.Salad = ₹70\n6.Soup = ₹60\n7.Tea = ₹10\n8.Coffee = ₹10\n".upper())
print("Please Select items from Menu")

# Initialize total amount
total = 0

while True:
    item_added = int(input("Please enter item number (enter '0' to check out): "))
    
    if item_added == 0:
        break  # 
    
    if 1 <= item_added <= 8:
        print("Item added to cart")
        if item_added == 1:
            total += 30
        elif item_added in [2, 3]:
            total += 40
        elif item_added == 4:
            total += 100
        elif item_added == 5:
            total += 70
        elif item_added == 6:
            total += 60
        elif item_added in [7, 8]:
            total += 10
    else:
        print("Enter a valid item number")

# Display the total amount
print("Sub Total: ₹",total)
print("GST: ₹",total*1.182-total)
print("Total Amount: ₹",total * 1.18)