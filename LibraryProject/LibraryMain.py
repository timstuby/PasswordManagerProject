"""What's missing:
Error 1: When the file (.txt book) is not named the same as what def create_book_list(): finds for the author
as the function will only take the part of the book name that is on the same line as "title:  " in the text file.
Login Issue: No safeguard against 2 users having the same username. This will cause only 1 user to be able to sign in.
"""


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
                year_published = line.split(':')[1].strip() #This doesn't work -- it'll take the publishing house instead of the year

            # Stop if we have all the information
            if title and author and year_published:
                break

        # Use defaults if information is not found
        title = title or 'Title Not Found'
        author = author or 'Author Not Found'
        year_published = year_published or 'Date Not Available'

        book_list.append(Book(title, author, year_published, False))

    return book_list
def print_page(book_text, start_line):
  """Displays a 30-line page from the given book text."""
  end_line = min(start_line + 30, len(book_text.splitlines()))
  page_text = '\n'.join(book_text.splitlines()[start_line:end_line])
  print(page_text)

def read_book(book, book_text):
  """Allows the user to read the selected book."""
  start_line = 0
  done = False

  while not done:
    print_page(book_text, start_line)
    print("\nOptions: 1 (Next Page), 2 (Previous Page), q (Quit)")
    choice = input()

    if choice == '1':
      start_line += 30  # Move to the next page
    elif choice == '2':
      start_line = max(0, start_line - 30)   # Move back a page
    elif choice == 'q':
      done = True
    else:
      print("Invalid input.")

def display_books(book_list):
    """Displays available books"""
    if not book_list:
        print("No books in the library currently.")
        return

    print("Available Books:")
    for i, book in enumerate(book_list):
        print(f"{i + 1}. {book.title} by {book.author}")

def experience(book_list):
    """Guides the user through the library experience"""
    done = False
    while not done:
        print("""What would you like to do? 
        1. View books in our library. 
        2. Borrow a book.
        3. Return a book.
        q. Quit""")

        choice_experience = input()

        if choice_experience == '1':  # View books
            display_books(book_list)

        elif choice_experience == '2':  # Borrow a book
            display_books(book_list)
            while True:
                try:
                    book_choice = int(input("Select a book by number: "))
                    if 0 < book_choice <= len(book_list):  # Check for valid input
                        selected_book = book_list[book_choice - 1]
                        if selected_book.checked_out:
                            print("This book is already checked out.")
                        else:
                            selected_book.checking_out()
                            print("Book successfully checked out.")

                            read_choice = input("Would you like to read the book now? (y/n): ")
                            if read_choice.lower() == 'y':
                                book_name = selected_book.title  # Get the title for lookup
                                read_book(selected_book, book_dict[book_name])
                        break  # Exit the loop on successful selection
                    else:
                        print("Invalid book selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice_experience == '3':  # Return a book
            display_books(book_list)
            while True:
                try:
                    book_choice = int(input("Select a book to return by number: "))
                    if 0 < book_choice <= len(book_list):
                        selected_book = book_list[book_choice - 1]
                        if not selected_book.checked_out:
                            print("This book is not currently checked out.")
                        else:
                            selected_book.returning()
                            print("Book successfully returned.")
                        break
                    else:
                        print("Invalid book selection.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

        elif choice_experience == 'q':
            done = True
            print("Thanks for visiting.")
        else:
            print("Invalid input.")
    print("All books have been returned.\n")


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
        print("Thanks for using this program.")
        exit()

# Example usage (remains the same)
folder_name = 'PlainTextBooks'
book_dict = create_book_dictionary(folder_name)
my_book_list = create_book_list(book_dict)
experience(my_book_list)