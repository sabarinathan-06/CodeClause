import sqlite3

# Create a database and table to store user information
conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

# Create a database and table to store books
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL
    )
''')
conn.commit()

# User management functions
def register_user(username, password):
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()

def login_user(username, password):
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    return cursor.fetchone()

# Book management functions
def add_book(title, author):
    cursor.execute('INSERT INTO books (title, author) VALUES (?, ?)', (title, author))
    conn.commit()

def remove_book(book_id):
    cursor.execute('DELETE FROM books WHERE id=?', (book_id,))
    conn.commit()

# User interface
def main():
    while True:
        print("\nLibrary Management System")
        print("1. Login")
        print("2. Register")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = login_user(username, password)
            if user:
                print(f"Welcome, {username}!")
                book_management()
            else:
                print("Invalid username or password.")

        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            register_user(username, password)
            print("Registration successful. You can now log in.")

        elif choice == '3':
            conn.close()
            print("Goodbye!")
            break

def book_management():
    while True:
        print("\nBook Management")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            add_book(title, author)
            print(f"Book '{title}' by {author} added successfully.")

        elif choice == '2':
            book_id = input("Enter the ID of the book to remove: ")
            remove_book(book_id)
            print("Book removed successfully.")

        elif choice == '3':
            print("Logging out.")
            break

if __name__ == "__main__":
    main()
