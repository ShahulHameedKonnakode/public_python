"""Phone Book Project: 
About project:this project ....."""
# main dictionary
phone_book={}
# Display Options
while True:
    print("1. Add Contact\n2. View\n3. Update\n4. Delete\n5. Display All")
    option=int(input("Please Select an option:  "))

    # add contact
    if option==1:
        contact={}

        name=input("Enter the name: ")
        #to store multiple phone numbers
        ph=[]
        count=int(input("How many phone numbers to save"))
        for i in range(count):
            phone=input("Enter phone number: ")
            if len(phone)!=10:
                print("please enter a valide phone number")
            
            else:
                ph.append(phone)
        #to store multiple emails  
        count=int(input("How many emails to save: "))#2
        em=[]
        for i in range(count):
            email=(input("Enter email address: "))
            em.append(email)
            print("Your contact is saved successfully")
        # store all to sub dictionary
        contact["Name"]=name
        contact["Phone"]=ph
        contact["Email"]=em
        phone_book[name]=contact
    

        #view
    elif option==2:
        data=input("Enter the contact name do you want to view:  ")
        print (phone_book[data])

    # upadation
    elif option==3:
        contact_name_update=input("Enter the contact name do you want to update:  ")

        # check to availabe in phone book
        if contact_name_update in phone_book:
            value_to_update=input("Enter the data item do you want to update\nName\nContact\nEmail")
            data_to_change=input("Enter the data to change:  ")
            phone_book[contact_name_update].update({value_to_update:data_to_change})
            print("Your contact is updated successfully")
            print(phone_book[contact_name_update])
        else:
            print("This contact not available")          
    #delete an item
    elif option==4:
        contact_name_to_delete=input("Enter the contact name do you want to update:  ")
        if contact_name_to_delete in phone_book:
            del phone_book[contact_name_to_delete]
            print("Your contact is updated successfully")
            print(phone_book[contact_name_to_delete])
        else:
            print("This contact not available")         
    # display all
    elif option==5:
        for x, y in phone_book.items():
            print(x,y)





    
    






