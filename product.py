from sqlalchemy import create_engine, Column, Float, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv
from datetime import datetime


engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Product(Base):
    __tablename__ = 'Products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_quantity = Column(Integer)
    product_price = Column(Integer)
    date_updated = Column(DateTime)

    def __repr__(self):
        return f'{self.product_name}, Qty= {self.product_quantity}, Price= {self.product_price}, Update= {self.date_updated}'

def cleansheet():
    with open('store-inventory/inventory.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter= '|')
        rows = list(reader)
        csvlist = []
        for row in rows:
            newnie = row[0].split(',')
            if len(newnie) == 5:
                newnie[0] = newnie[0] + "," + newnie[1]
                newnie.remove(newnie[1])
            csvlist.append({'product': newnie[0], 'price': newnie[1], 'quantity': newnie[2], 'date': newnie[3]})

        del csvlist[0]
        dougie = []
        for item in csvlist:
            nougie = {'product': None, 'price' : None, 'quantity': None, 'date': None }
            nougie['product'] = item['product']
            item['price'] = item['price'].replace('$', '')
            nougie['price'] = int(item['price'].replace('.', ''))
            nougie['quantity'] = int(item['quantity'])
            nougie['date'] = datetime.strptime(item['date'], '%m/%d/%Y')
            dougie.append(nougie)
        return dougie

def dictadder(data):
    dumper = []
    for item in data:
        iname = item['product']
        ipq = item['quantity']
        iprice = item['price']
        date = item['date']
        prod = Product(product_name = iname, product_quantity=ipq, product_price=iprice, date_updated=date)
        if session.query(Product).first():
            if matchchecker(prod):
               if prod.date_updated >= matchchecker(prod).date_updated:
                    session.query(Product).filter(Product.product_name == matchchecker(prod).product_name).update({
                        'product_quantity': prod.product_quantity, 'product_price': prod.product_price,'date_updated': date})
            else:
                 session.add(prod)
                 session.commit()
        else:
            session.add(prod)
            session.commit()

def matchchecker(psearch):
    for item in session.query(Product):
        if str(item.product_name).lower() == str(psearch.product_name).lower():
            return item


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    dictadder(cleansheet())
    for i in session.query(Product):
        print(i)
    dictadder(cleansheet())
    for i in session.query(Product):
        print(i)
