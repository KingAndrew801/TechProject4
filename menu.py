import csv
import string
from datetime import datetime, date
from product import Base, Product, session, engine
import re




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
    trying = True
    while trying == True:
        try:
            prodname = input("Please type the product name:  ")
            if prodname.isalpha() == True:
                trying = False
            if prodname.isalpha() == False:
                raise ValueError("You must enter letters for the name!")
        except ValueError as err:
            print(err)

    trying = True
    while trying == True:
        try:
            prodq = input("Now please input the product quantity:  ")
            if prodq.isdigit() == True:
                trying = False
            if prodq.isdigit() == False:
                raise ValueError('Qunatity must be a whole number')
        except ValueError as err:
            print(err)

    trying = True
    while trying == True:
        try:
            prodprice = float(input("Now enter the price of the product:  "))
            checkprod = "{:.2f}".format(prodprice).split('.')
            if len(checkprod[1]) == 2:
                trying = False
            else:
                raise ValueError('You must enter the price in a valid price format (example 1.00)')
        except ValueError as err:
            print(err)
    pdate = date.today()
    if session.query(Product).filter(product_name= prodname) == prodname:
        session.query(Product).filter(product_name=prodname).delete()
    session.add(Product(product_name = prodname, product_quantity=prodq, product_price=prodprice, date_updated=pdate))

def backup():
    with open('backup.db', 'a') as csvfile:
        fieldnames = ['product_name', 'product_id', 'product_quantity', 'product_price', 'date_updated']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in session.query(Product):
            writer.writerow({
                'product_name': item[0], 'product_id': item[1],
                'product_quantity': item [2], 'product_price': item[3],
                'date_updated':item[4]})

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
    # addprod()
    backup()
    # for i in session.query(Product):
    #     print(i)