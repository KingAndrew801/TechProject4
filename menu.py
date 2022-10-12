import sqlite3

def viewprod():
    running = True
    while running == True:
        connection = sqlite3.connect("inventory.db")
        crsr = connection.cursor()
        print("\nPlease enter a product name or product ID")
        choice = input("Enter selection:   ")
        if choice == int:
            for item in crsr.execute(f"select * from Products where product_id = {choice}"):
                print(item)
        if choice == str:
            for item in crsr.execute(f"select * from Products where product_name like '{choice}%'"):
                print(item)
        try:
            choice = input("Do you want to search again? (Y/N)  ").lower()
            if choice == 'y':
                continue
            if choice == 'n':
                break
            else:
                raise ValueError("You must select either Y or N")
        except ValueError as err:
            print(err)


def menu():
    print('''
----------Inventory Application----------
Make a selection from the following:
V = view the details of a single product
A = add a new product to the database
B = make a backup of the database.
''')
    choice = input("Enter selection:   ")

if __name__ == '__main__':
    # menu()
    viewprod()