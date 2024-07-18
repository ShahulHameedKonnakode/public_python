# MyJava Café wants you to write a program to take orders from the Internet. Your program 
# asks for the item, its price, and if overnight shipping is wanted. Regular shipping for items under
# $10 is $2.00; for items $10 or more shipping is $3.00. For overnight delivery add $5.00. For 
# example, the output might be:
# Enter the item : Tuna Salad
# Enter the price : 450
# Overnight delivery (0==no, 1==yes): 1
# Invoice: Tuna Salad 4.50
#  Shipping 7.00
#  Total 11.50

print("MY JAVA CAFE")
print("*************")

print('Our Favourit Items')
print("*************")
print("1.Burger = ₹130\n2.Pizza = ₹400\n3.Chicken Nuggets = ₹60\n4.French Fries = ₹100\n5.Salad = ₹70\n6.Soup = ₹60\n7.Mandi = (Full:₹650, Half: ₹350, Quarter:₹240)\n8.Fruit Salad = ₹190\n".upper())
print("Please Select items from Menu")
cart={}
total=0
while True:
    option=int(input("Please Select Item numbers (Enter 0 for Checkout): "))
    

   
    if 1<= option <=8:
        print("Item Added to Cart")
        items={}
        subcart=[]
        
        if option==1:
            subcart.append("1.Burger = ₹130")
            total+=130        
        elif option==2:
            subcart.append("2.Pizza = ₹400")
            total+=400
        elif option==3:
            subcart.append("3.Chicken Nuggets = ₹60")
            total+=60
        elif option==4:
            subcart.append("4.French Fries = ₹100")
            total+=100
        elif option==5:
            subcart.append("5.Salad = ₹70")
            total+=70
        elif option==6:
            subcart.append("6.Soup = ₹60")
            total+=60
        elif option==7:
            mandiqty=int(input("7.1: Full\n 7.2: Half\n 7.3: Quarter"))
            if mandiqty==7.1:
                subcart.append("7.Mandi-Full")
                total+=650
            if mandiqty==7.2:
                subcart.append("7.Mandi-Half")
                total+=350
            if mandiqty==7.3:
                subcart.append("7.Mandi-Quarter")
                total+=240
            else:
                print("Quantity Not Available")
        elif option==8:
            subcart.append("8.Fruit Salad = ₹190")
            total+=190
        else:
            print("Please Enter a Valid Option")
    else:
            print("Please Enter a Valid Option") 
    for i in range(option):
        items["Item"]=subcart
        cart[option]=items
    if option==0:      
        
        print("Total Items in Cart")
        print(cart)
        print("Sub Total: ₹",total)  
        print("Delivery Options")
        print("*************")
        print("11.Regular\n12.Express\n13.Over Night")
        print("*************")
        delivery_option=int(input("Select Any Option: "))
        
        delivery_charge=0
        if delivery_option==11:
            delivery_charge+=10*len(cart)
        elif delivery_option==12:
            delivery_charge+=20*len(cart)
        elif delivery_option==13:
            delivery_charge+=30*len(cart)
           


            print("Sub Total: ₹",total)
            print("Shipping: ₹",delivery_charge)
            print("GST: ₹",round(total*1.182-total,2))
            
            print("Total Amount: ₹",round((total * 1.18),2))
        
            print("Payment Options")
            print("*************")
            print("14.UPI\n15.Cash on Delivery\n16.Card Payment")
            print("*************")
            payment_option=int(input("Select Any Option: "))
            if payment_option==14:
                print("Our UPI Payment Number is 9544837026. Please Pay on This Number.")
                print("*************")
                print("Thank You...! Order Again...!! Have a Nice Day.")
            elif payment_option==15:
                print("Please Hand Over the Cash to Our Delivery Agent.")
                print("*************")
                print("Thank You...! Order Again...!! Have a Nice Day.")
            elif payment_option==16:
                print("You Can Use Debit or Credit Card for Card Payment. Don't Share Your Creditial Details to Anonymous Persons.")
                print("*************")
                print("Thank You...! Order Again...!! Have a Nice Day.")
                break 
                
            else:
                print("Please Enter a Valid Option")
        else:
            print("Please Enter a Valid Option")   
            
                
    
        
        
        
                

    