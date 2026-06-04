FILE_NAME = "books.txt"

# ---------------- LOGIN ----------------
def login():
    print("=== LOGIN SYSTEM ===")
    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Login!")
        return False


# ---------------- ADD BOOK ----------------
def add_book():
    try:
        book_id = input("Enter Book ID: ")

        # check unique ID
        with open(FILE_NAME, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[0] == book_id:
                    print("Book ID already exists!")
                    return

        name = input("Book Name: ").title()
        author = input("Author Name: ").title()
        price = float(input("Price: "))
        qty = int(input("Quantity: "))

        if price < 0 or qty < 0:
            print("Price/Quantity cannot be negative!")
            return

        status = "Available" if qty > 0 else "Out of Stock"

        with open(FILE_NAME, "a") as f:
            f.write(f"{book_id},{name},{author},{price},{qty},{status}\n")

        print("Book Added Successfully!")

    except:
        print("Invalid Input!")


# ---------------- VIEW BOOKS ----------------
def view_books():
    try:
        with open(FILE_NAME, "r") as f:
            print("\n--- ALL BOOKS ---")
            for line in f:
                print(line.strip())

    except:
        print("No books found!")


# ---------------- SEARCH BOOK ----------------
def search_book():
    book_id = input("Enter Book ID to search: ")

    found = False

    with open(FILE_NAME, "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[0] == book_id:
                print("\nBook Found:")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Author:", data[2])
                print("Price:", data[3])
                print("Qty:", data[4])
                print("Status:", data[5])
                found = True
                break

    if not found:
        print("Book Not Found!")


# ---------------- UPDATE BOOK ----------------
def update_book():
    book_id = input("Enter Book ID to update: ")

    books = []
    found = False

    with open(FILE_NAME, "r") as f:
        books = f.readlines()

    with open(FILE_NAME, "w") as f:
        for line in books:
            data = line.strip().split(",")

            if data[0] == book_id:
                print("1. Update Name")
                print("2. Update Price")
                print("3. Update Quantity")

                choice = input("Enter choice: ")

                if choice == "1":
                    data[1] = input("New Name: ").title()

                elif choice == "2":
                    data[3] = input("New Price: ")

                elif choice == "3":
                    data[4] = input("New Quantity: ")
                    data[5] = "Available" if int(data[4]) > 0 else "Out of Stock"

                found = True
                print("Book Updated!")

            f.write(",".join(data) + "\n")

    if not found:
        print("Book Not Found!")


# ---------------- DELETE BOOK ----------------
def delete_book():
    book_id = input("Enter Book ID to delete: ")

    with open(FILE_NAME, "r") as f:
        books = f.readlines()

    with open(FILE_NAME, "w") as f:
        found = False

        for line in books:
            data = line.strip().split(",")

            if data[0] != book_id:
                f.write(line)
            else:
                found = True

    if found:
        print("Book Deleted!")
    else:
        print("Book Not Found!")


# ---------------- ANALYZE DATA ----------------
def analyze_data():
    try:
        with open(FILE_NAME, "r") as f:
            prices = []
            total = 0
            available = 0
            out = 0

            for line in f:
                data = line.strip().split(",")

                price = float(data[3])
                qty = int(data[4])

                prices.append(price)
                total += 1

                if qty > 0:
                    available += 1
                else:
                    out += 1

        if total == 0:
            print("No data")
            return

        print("\n--- ANALYSIS ---")
        print("Total Books:", total)
        print("Average Price:", sum(prices)/total)
        print("Most Expensive:", max(prices))
        print("Cheapest:", min(prices))
        print("Available Books:", available)
        print("Out of Stock:", out)

    except:
        print("No data found!")


# ---------------- MAIN MENU ----------------
def main():
    if not login():
        return

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Update Book")
        print("5. Delete Book")
        print("6. Analyze Data")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            analyze_data()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid Choice!")


main()