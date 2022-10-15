
import string
from datetime import datetime
from product import Base, Product, session, engine




def viewprod():
    running = True
    while running == True:
        print("\nPlease enter a product name or product ID")
        choice = input("Enter selection:   ")
        if choice.isalpha():
            choice = choice + '%'
            for item in session.query(Product).filter(Product.product_name.like(choice)):
                print(item)
        else:
            for item in session.query(Product).filter(Product.product_id == int(choice)):
                print(item)
        try:
            choice = input("Do you want to search again? (Y/N)  ").lower()
            if choice == 'y':
                continue
            if choice == 'n':
                running = False
                break
            else:
                raise ValueError("You must select either Y or N")
        except ValueError as err:
            print(err)

def addprod():
    try:
        prodname = input("Please type the product name:  ")
        if prodname.isalpha() == False:
            raise ValueError("You must enter letters for the name!")
    except ValueError as err:
        print(err)

    try:
        prodq = input("Now please input the product quantity:  ")
        if prodq.isdigit() == False:
            raise ValueError('Qunatity must be a whole number')
    except ValueError as err:
        print(err)
    try:
        prodprice = input("Now enter the price of the product:  ")
        if isinstance(prodprice, float) == False:
            raise ValueError('You must enter the price in a valid price format')
    except ValueError as err:
        print(err)
        date = datetime.today
    session.add(Product(product_name = prodname, product_quantity=prodq, product_price=prodprice, date_updated=date))



def backup():
    pass

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
    # viewprod()
    addprod()
