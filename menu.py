import csv
from datetime import datetime

import product
from product import Base, Product, session, dictadder, cleansheet, engine, matchchecker


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
            if session.query(Product).filter(Product.product_id == int(choice)).one_or_none():
                 for item in session.query(Product).filter(Product.product_id == int(choice)):
                    print(item)
            else:
                print('There is no product with that ID number.')
        try:
            choice = input("Do you want to search for another product? (Y/N)  ").lower()
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
    prodname = input("Please type the product name:  ")
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
    pdate = datetime.today()
    prod = Product(product_name = prodname, product_quantity=prodq, product_price=prodprice, date_updated=pdate)
    if matchchecker(prod):
        if matchchecker(prod).date_updated <= prod.date_updated:
            session.query(Product).filter(Product.product_id == matchchecker(prod).product_id).update({
                        'product_quantity': prod.product_quantity, 'product_price': prod.product_price})
            print('\n Your product has been updated!')
        else:
            pass
    else:
        session.add(prod)
        session.commit()
        print('\n Your product has been added to the database!')

def backup():
    with open('backup.csv', 'a', newline='') as csvfile:
        fieldnames = [ 'product_name', 'product_price', 'product_quantity', 'date_updated']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in session.query(Product):
            if len(str(item.product_price)) >= 3:
                newp =  '$' + str(item.product_price)[:-2] + '.' + str(item.product_price)[1:]
            if len(str(item.product_price)) == 2:
                newp = '$' + '0.' + str(item.product_price)
            if len(str(item.product_price)) == 1:
                newp = '$' + '0.0' + str(item.product_price)
            writer.writerow({
                'product_name': item.product_name,
                'product_price': newp, 'product_quantity': item.product_quantity,
                'date_updated':str(datetime.strftime(item.date_updated, '%m/%d/%Y'))})

def menu():
    dictadder(product.cleansheet())
    running = True
    while running:
        while running:
            try:
                print('''
----------Inventory Application----------
Make a selection from the following:
V = view the details of a single product
A = add a new product to the database
B = make a backup of the database.
                ''')
                choice2 = input("Enter selection:   ").lower()
                if choice2 == 'v':
                    viewprod()
                    break
                if choice2 == 'a':
                    addprod()
                    break
                if choice2 == 'b':
                    backup()
                    break
                else:
                    raise ValueError("You must enter either v, a, or b")
            except ValueError as err:
                print(err)
        trying2 = True
        while trying2:
            try:
                choice = input('Do you want to choose again?(Y/N):  ').lower()
                if choice == 'y':
                    break
                if choice == 'n':
                    running = False
                    break
                else:
                    raise ValueError("You must enter either y or n")
            except ValueError as err:
                print(err)

if __name__ == '__main__':
    menu()