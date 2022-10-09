from sqlalchemy import create_engine, Column, Float, Integer, Date, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite3:///inventory.db', echo=True)
Base = declarative_base()

class Product(Base):
    if __name__ == '__main__':
        product_id = Column(Integer, primary_key=True)
        product_name = Column(String)
        product_quantity = Column(Integer)
        product_price = Column(Float)
        date_updated = Column(Date)

        def __repr__(self):
            return f'{self.product_name}, Qty= {self.product_quantity}, Price= {self.product_price}, Update= {self.date_updated}'

if __name__ == '__main__':
    Base.metadata.create_all(engine)
