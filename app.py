import menu
from product import Base, engine
menu.menu()

if __name__ == '__main__':
    Base.metadata.create_all(engine)