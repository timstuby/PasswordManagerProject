# Exercise using the class function, (not seen in class).

# Objective: Build a functioning library system.
# TODO 1: Add book donation option
# TODO 2: Add user login.
# TODO 3: Add more book options
# TODO 4 (maybe): Add the actual text from the books as files.
    # TODO 4(cont): Add ways to disect the book, like counting number of words

punctuation = ".,!?\n"
# User login.
def account_creation():
    with open("UserLogins.txt", 'a') as file:
        print("Enter your choice of username: ")
        username = input("")
        file.write(f"{username}\n")
        print("Enter your password: ")
        password = input("")
        file.write(f"{password}#\n\n")
        print("Account successfully created.")

def extract_credentials(file_path):
    credentials = {}

    with open(file_path, 'r') as file:
        lines = file.readlines()
        i = 0
        while i < len(lines):
            # Extract username and password
            username = lines[i].strip()
            password = lines[i + 1].strip()

            # Add to dictionary
            credentials[username] = password

            # Move to next set of credentials
            i += 4  # There are 3 new lines between passwords

    return credentials

def login():
    credentials = {}
    with open("UserLogins.txt", 'r') as file:
        for line in file:

        print("Enter your username.")
        username = input("")
#def login():
 #   credentials = extract_credentials("UserLogins.txt")
    
  #  print("Enter your username:")
   # username = input("")
    # print("Enter your password:")
   # password = input("")

    # if username in credentials and credentials[username] == password:
    #    print("Login successful!")
    #else:
    #    print("Invalid username or password.")


print("""Welcome to the Library! What would you like to do:
1. Create a new account. 
2. Login to your account.
q. Quit""")
done = False
LoginChoice = input("Enter your choice: ")
while not done:
    if LoginChoice == '1':
        account_creation()
        done = True
    elif LoginChoice == '2':
        login()
    elif LoginChoice == 'q':
        done = True
        print("Thanks for visiting")



# Book system
class Book:   # 'Class' is a template that we have not learned in class.
    def __init__(self, title, author, ISBN, year_published, genre, pages, checked_out):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.year_published = year_published
        self.genre = genre
        self.pages = pages
        self.checked_out = checked_out
    def get_age(self):
        import datetime
        current_year = datetime.datetime.now().year
        return current_year - self.year_published

    def checking_out(self):
        self.checked_out = True
    def returning(self):
        self.checked_out = False

    def check_checked_out(self):
        return self.checked_out



book1 = Book("The Hobbit", "J.R.R. Tolkien", "9780482103", 1937, "Fiction", 550, True)
book2 = Book("Pride and Prejudice", "Jane Austen", "9780482101923", 1813, "Non-Fiction", 340, False)


def experience():
    done = False
    while not done:
        print("""What would you like to do? 
        1. View books in our library. 
        2. Return a book.
        q. Quit""")
        choice_experience = input()
        if choice_experience == '1':
            print(f"The books are {book1.title}, {book2.title}")
            print("Which book would you like to select?")
            book_choice = int(input("Insert a number: "))
            if book_choice == 1:
                print(book1.title, "by", book1.author)
                print("This book is", book1.get_age(), "years old")
                if book1.check_checked_out() == False:
                    print("This book is available, would you like to borrow it?")
                    choice = input("Type 'Yes or No': ")
                    if choice == "Yes":
                        book1.checking_out()
                    else:
                        print("Thanks for visiting!")
                else:
                    print("This book is checked out.")
            elif book_choice == 2:
                print(book2.title, "by", book2.author)
                print("This book is", book2.get_age(), "years old")
                if book2.check_checked_out() == False:
                    print("This book is available, would you like to borrow it?")
                    choice = input("Type 'Yes or No': ")
                    if choice == "Yes":
                        book2.checking_out()
                        print("Book successfully checked out.")
                    else:
                        print("Thanks for visiting!")
                else:
                    print("This book is checked out.")
        elif choice_experience == '2':
            print(f"The books are {book1.title}, {book2.title}")
            print("Which book would you like to return?")
            book_choice = int(input("Insert a number: "))
            if book_choice == 1:
                if book1.check_checked_out() == False:
                    print("This book has not been checked out...")
                else:
                    print("Returning book...")
                    book1.returning()
            elif book_choice == 2:
                if book2.check_checked_out() == False:
                    print("This book has not been checked out...")
                else:
                    print("Returning book...")
                    book2.returning()
            else:
                print("Invalid book input.")
        elif choice_experience == 'q':
            done = True
            print("Thanks for visiting.")
        else:
            print("Invalid book input.")

experience()
