import datetime

# Class to represent a library member
class Member:
    def __init__(self, member_id, name, place, mob):
        # Initializing member attributes
        self.name = name
        self.place = place
        self.mob = mob
        self.member_id = member_id

# Class to manage all members in the library
class Total_Members:
    def __init__(self):
        # Directory to store members and a starting ID for new members
        self.members_directory = []
        self.new_id = 2001

    # Function to generate a new member ID
    def generate_member_id(self):
        member_id = self.new_id
        self.new_id += 1
        return member_id
    
    # Function to add a new member to the directory
    def add_member(self, member_details):
        self.members_directory.append(member_details)
        print(f"✅ You have registered Successfully: \nMembership No.{member_details.member_id}\n{member_details.name}\n{member_details.place}\n{member_details.mob}\nKeep in mind for the further reference. ")

    # Function to check if a member exists by their ID
    def check_member(self, member_id):
        for member in self.members_directory:
            if member.member_id == member_id:
                return member
        # Print if the member is not found
        print("Member not found")

    # Function to update member details (name, place, or mobile number)
    def update_member_details(self, member_id):
        member_to_update = membership.check_member(member_id)
        if member_to_update:
            print("Which type of data do you want to update? \n1. Name\n2. Place\n3. Mob")
            option_to_change = int(input("Enter your choice: "))
            
            if option_to_change == 1:
                member_new_name = input("Enter New Name: ")
                member_to_update.name = member_new_name
                print("Name is updated successfully. ✅")

            if option_to_change == 2:
                member_new_place = input("Enter New Place: ")
                member_to_update.place = member_new_place
                print("Place is updated successfully. ✅")

            if option_to_change == 3:
                member_new_mob = int(input("Enter New Mob: "))
                member_to_update.mob = member_new_mob
                print("Mobile Number is updated successfully. ✅")

    # Function to remove a member from the directory
    def remove_member(self, member_id):
        member_to_remove = membership.check_member(member_id)
        if member_to_remove:
            self.members_directory.remove(member_to_remove)
            print(f"{member_to_remove.name} is removed successfully.")
        else:
            print("Member not found")

    # Function to display all members in the directory
    def display_total_members(self):
        for member in self.members_directory:
            print(f"No. {member.member_id}, Name: {member.name}, Place: {member.place}, Phone: {member.mob}")
        else:
            print("No members available in Directory")

# Class to represent a book in the library
class Book:
    def __init__(self, serial_no, name, author, genre):
        # Initializing book attributes
        self.name = name
        self.author = author
        self.genre = genre
        self.serial_no = serial_no

# Class to manage the library operations
class Library:    
    def __init__(self):
        # Initializing the library database, issue register, serial number, and fine amount
        self.library_database = []
        self.issued_book_register = []
        self.new_serial_number = 1001
        self.fine_amount = 5

    # Function to generate a new serial number for books
    def generate_serial_no(self):
        serial_no = self.new_serial_number
        self.new_serial_number += 1
        return serial_no
    
    # Function to add a new book to the library database
    def add_book(self, book_details):
        self.library_database.append(book_details)
        print(f"The Book: No.{book_details.serial_no} {book_details.name}, by {book_details.author}, Genre: {book_details.genre} is Successfully Added to Library. ✅")
    
    # Function to check if a book exists by its serial number
    def check_book(self, book_access_no):
        for book in self.library_database:
            if book.serial_no == book_access_no:
                return book
        # Print if the book is not found
        print("⚠️ Book is not available")

    # Function to issue a book to a member
    def issue_book(self, member_id, book_access_no):
        book_to_issue = self.check_book(book_access_no)
        member_to_issue = membership.check_member(member_id)
        if book_to_issue and member_to_issue:
            self.issued_date = datetime.datetime.now()
            self.issued_book_register.append((member_to_issue, book_to_issue, self.issued_date))
            print(f"{book_to_issue.name} is issued to {member_to_issue.name} on {self.issued_date.strftime('%Y-%m-%d %H:%M:%S')}.")
        else:
            print(" ⚠️ Cannot issue book. Member or book not found.")   

    # Function to return a book issued to a member and calculate any fines
    def return_book(self, member_id, book_access_no):
        book_to_return = self.check_book(book_access_no)
        member_to_return = membership.check_member(member_id)
        if book_to_return and member_to_return:
            for issued_record in self.issued_book_register:
                issued_member, issued_book, issued_date = issued_record
                if issued_book == book_to_return and issued_member == member_to_return:
                    self.return_date = datetime.datetime.now()
                    self.total_duration = (self.return_date - issued_date).days
                    if self.total_duration > 0:
                        fine = self.total_duration * self.fine_amount
                        while True:
                            print(f"� Sorry, You delayed returning the book. Please pay the fine amount: {fine}")
                            print("PAY NOW")
                            option = int(input("1. Yes\n2. No: "))
                            if option == 1:                        
                                self.issued_book_register.remove(issued_record)
                                print(f"{book_to_return.name} is returned by {member_to_return.name} and the fine amount of {fine} has been paid. Thank You. � ")
                                break
                            elif option == 2:
                                print("⚠️ Please return the book and pay the fine.�")
                            else:
                                print("⚠️ Invalid option.")
                    else:
                        # If no fine is needed (book returned on the same day or earlier)
                        self.issued_book_register.remove(issued_record)
                        print(f"{book_to_return.name} is returned by {member_to_return.name}. No fine needed.")
                    return  # Exit after processing the correct record
                    
            print("⚠️ This book was not issued to this member.")
        else:
            print("⚠️ Cannot return book. Member or book not found.")

    # Function to display all books in the library catalogue
    def display_catalogue(self):
        for book in self.library_database:
            print(f"No.{book.serial_no} {book.name}, by {book.author}, Genre: {book.genre}")

    # Function to handle the library management menu
    def library_management(self):
        while True:
            print("\n �Library Management🔰 \n")
            library_management_menu = {
                "1": "Add Book",
                "2": "OPAC (Check Book Status)",
                "3": "Issue Book",
                "4": "Return Book",
                "5": "Catalogue",
                "6": "Main Menu"
            }
            for key, value in library_management_menu.items():
                print(f"{key}.{value}")
            library_menu_option = int(input("\n✳️  Enter Your Choice: "))
            if library_menu_option == 1:
                name = input("Enter the Book Name: ")
                author = input("Enter the Author Name: ")
                genre = input("Enter the Genre: ")
                serial_no = library.generate_serial_no()
                book_details = Book(serial_no, name, author, genre)
                library.add_book(book_details)

            elif library_menu_option == 2:
                book_access_no = int(input("Enter Access Number of Book: "))
                checked_book = library.check_book(book_access_no)
                status = "Available" if checked_book not in self.issued_book_register else "issued"
                print(f"\n� Book Details:\nThe Book: No.{checked_book.serial_no} {checked_book.name} by {checked_book.author} is {status}✅")
            
            elif library_menu_option == 3:
                member_to_issue = int(input("Enter the member id : "))
                book_to_issue = int(input("Enter Access Number of Book: "))
                library.issue_book(member_to_issue, book_to_issue)

            elif library_menu_option == 4:
                member_to_return = int(input("Enter the member id : "))
                book_to_return = int(input("Enter Access Number of Book: "))
                library.return_book(member_to_return, book_to_return)

            elif library_menu_option == 5:
                library.display_catalogue()
            
            elif library_menu_option == 6:
                main_functions()  # Go back to the main menu
            else:
                print("⚠️ Please Enter a Valid Option")

    # Function to handle the subscription management menu
    def subscription_management(self):
        while True:
            print("\n �Subscription Management🔰 \n")
            subscription_management_menu = {
                "1": "Add Member",
                "2": "Check Member",
                "3": "Update Member's Details",
                "4": "Remove Member",
                "5": "Total Members List",
                "6": "Main Menu"
            }
            for key, value in subscription_management_menu.items():
                print(f"{key}.{value}")
            subscription_menu_option = int(input("\n✳️  Enter Your Choice: "))

            if subscription_menu_option == 1:
                member_id = membership.generate_member_id()
                member_name = input("Enter the Full Name of Applicant: ")
                member_place = input("Enter Place: ")
                try:
                    member_mob = int(input("Enter Phone Number: "))
                    
                    # Create a Member object and add it to the directory
                    member_details = Member(member_id, member_name, member_place, member_mob)
                    membership.add_member(member_details)
                except ValueError:
                    print("⚠️ Enter a Valid Phone Number")
            

            elif subscription_menu_option == 2:
                member_to_check = int(input("Enter the member id do you want to check: "))
                member = membership.check_member(member_to_check)
                if member:
                    print(f"\nMember Details:\nMembership No.{member.member_id}\n{member.name}\n{member.place}\n{member.mob}")

            elif subscription_menu_option == 3:
                member_to_update = int(input("Enter the member id do you want to update: "))
                membership.update_member_details(member_to_update)

            elif subscription_menu_option == 4:
                member_to_remove = int(input("Enter the member id do you want to update: "))
                membership.remove_member(member_to_remove)
                
            elif subscription_menu_option == 5:
                membership.display_total_members()

            elif subscription_menu_option == 6:
                main_functions()  # Go back to the main menu

            else:
                print("⚠️ Please Enter a Valid Option")

    # Function to display information about the library
    def about_us(self):
        print("""About Us \n Welcome to the APJ Abdul Kalam Memorial Central Library, a beacon of knowledge and inspiration dedicated to the memory of Dr. APJ Abdul Kalam, India’s beloved former President and renowned scientist. Our library is a sanctuary for learners, researchers, and book lovers, offering a vast collection of resources across various disciplines.
              
        At the APJ Abdul Kalam Memorial Central Library, we believe in the power of knowledge to transform lives. Our mission is to provide an inclusive and enriching environment that fosters intellectual growth and lifelong learning. We offer a diverse range of books, journals, digital resources, and multimedia materials to cater to the needs of our community.
        
        Our state-of-the-art facilities include quiet study areas, collaborative workspaces, and advanced research tools, ensuring that every visitor has access to the best possible resources. We also host regular events, workshops, and lectures to engage our patrons and promote a culture of continuous learning.
        
        Join us at the APJ Abdul Kalam Memorial Central Library, where knowledge meets inspiration, and together, let’s embark on a journey of discovery and growth.""")

    # Function to display help information
    def help_library(self):
        print("Please Follow me:\nwww.linkedin.com/in/shahul-hameed-konnakode-a04b38115")

# Main function to manage overall program flow
def main_functions():
    print("\n� APJ Abdul Kalam Memorial Central Library 📚\n\nMain Menu:")
    main_menu = {"1": "Library Management", "2": "Subscription Management", "3": "About Library", "4": "Help"}
    for key, value in main_menu.items():
        print(f"{key}.{value}")

    choice = int(input("\n⏩ Select an Option: "))

    if choice == 1:
        library.library_management()

    elif choice == 2:
        library.subscription_management()
    
    elif choice == 3:
        library.about_us()
    
    elif choice == 4:
        library.help_library()
    else:
        print("⚠️ Please Enter a Valid Option")

# Initialize the main classes
membership = Total_Members()
library = Library()

# Start the main loop to keep the program running
while True:
    main_functions()
    