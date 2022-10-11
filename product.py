from sqlalchemy import create_engine, Column, Float, Integer, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import csv

engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Product(Base):
    __tablename__ = 'Products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_quantity = Column(Integer)
    product_price = Column(Float)
    date_updated = Column(Date)

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
                print(newnie)
            csvlist.append({'product': newnie[0], 'price': newnie[1], 'quantity': newnie[2], 'date': newnie[3]})
        for item in csvlist:
            try:
                item['price'] = int(item['price'])
            except ValueError:
                del item
        print(csvlist)

if __name__ == '__main__':
    # Base.metadata.create_all(engine)
    cleansheet()
