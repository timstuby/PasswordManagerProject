# Exercise using the class function, (not seen in class).

# Objective: Build a functioning library system.

# TODO 4 (maybe): Add the actual text from the books as files.
    # TODO 4(cont): Add ways to disect the book, like counting number of words

punctuation = ".,!?\n"
# User login.

#TODO: Prevent user from writing to file unless both password and username are provided. Providing just one will cause the code not to work
def account_creation():
    with open("UserLogins.txt", 'a') as file:
        print("Enter your choice of username: ")
        username = input("")
        file.write(f"{username}\n")
        print("Enter your password: ")
        password = input("")
        file.write(f"{password}\n\n\n")
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
    credentials = extract_credentials("UserLogins.txt")
    attempts = 0
    while attempts != 4:
        print("Enter your username:")
        username = input("")
        print("Enter your password:")
        password = input("")
        if username in credentials and credentials[username] == password:
            print("Login successful!")
            break
        elif username in credentials and credentials[username] != password:
            print("Incorrect password, try again.")
            attempts += 1
        elif username not in credentials:
            print("That username does not exist")
            # The user doesn't make an attempt on the password here, so we don't count it as an attempt.
        elif username or password == "Quit":
            break
        else:
            print("Invalid username or password.")
            attempts += 1
    if attempts == 4:
        print("""The login process has failed due to too many incorrect attempts.
        Would you like to create a new account? 
        1. Create a new account
        2. Quit the program
        """)
        loop_fail = False  # used to catch invalid input
        while not loop_fail:
            fail_choice = input("Enter your choice: ")
            if fail_choice == "1":
                account_creation()
                break
            elif fail_choice == "2":
                print("Thanks for using this program.")
                exit()
            else:
                print("Invalid input, try again")


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
        done = True
    elif LoginChoice == 'q':
        done = True
        print("Thanks for using this program.")



# Book system
class Book:
    def __init__(self, title, author, year_published, checked_out):
        self.title = title
        self.author = author
        self.year_published = year_published
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

# Retrieve text from books and store into a dictionary:
import os

def create_book_dictionary(folder_name='PlainTextBooks'):  # Optional folder_name parameter
    """Creates a dictionary where keys are book names and values are the book's text.

    Args:
        folder_name (str): The name of the folder containing the book text files,
                           relative to the script's location. Defaults to 'books'.

    Returns:
        dict: A dictionary where keys are book filenames (without extension)
              and values are the corresponding file contents.
    """

    script_dir = os.path.dirname(__file__)  # Get the directory of the current script
    folder_path = os.path.join(script_dir, folder_name)

    book_dict = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):  # Assuming your book files are .txt
            book_name, _ = os.path.splitext(filename)  # Remove the '.txt' extension
            with open(os.path.join(folder_path, filename), 'r') as file:
                book_text = file.read()
                book_dict[book_name] = book_text

    return book_dict

def create_book_list(book_dict):
    book_list = []
    for i, (book_name, book_text) in enumerate(book_dict.items()):
        lines = book_text.splitlines()

        title = None
        author = None
        year_published = None

        for line in lines[:100]:  # Limit to the first 100 lines
            if line.startswith('Title:'):
                title = line.split(':')[1].strip()
            elif line.startswith('Author:'):
                author = line.split(':')[1].strip()
            elif line.startswith('Original publication:'):
                year_published = line.split(':')[1].strip()

            # Stop if we have all the information
            if title and author and year_published:
                break

        # Use defaults if information is not found
        title = title or 'Title Not Found'
        author = author or 'Author Not Found'
        year_published = year_published or 'Date Not Available'

        book_list.append(Book(title, author, year_published, False))

    return book_list

# Example usage
folder_name = 'PlainTextBooks'  # Adjust if needed
book_dict = create_book_dictionary('PlainTextBooks')
my_book_list = create_book_list(book_dict)

# Access your books:
for book in my_book_list:
    print(f"Title: {book.title}, Author: {book.author}")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 1937, True)
book2 = Book("Pride and Prejudice", "Jane Austen", 1813, False)


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
