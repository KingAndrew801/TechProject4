import menu

import csv
from datetime import date

import product
from product import Base, Product, session, dictadder, cleansheet, engine,starter


####experimentory import
from sqlalchemy import create_engine, Column, Float, Integer, Date, String
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
    product_price = Column(Float)
    date_updated = Column(Date)

    def __repr__(self):
        return f'{self.product_name}, Qty= {self.product_quantity}, Price= {self.product_price}, Update= {self.date_updated}'

menu.menu()