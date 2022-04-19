from sqlalchemy import Column, String, Integer
from database import Database


class Product(Database):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    brand = Column("brand", String)
    name = Column("name", String)
    composition = Column("composition", String)
    needle_size = Column("needle_size", String)
    price = Column("price", String)

    def __init__(self, brand, name, composition, needle_size, price):
        self.brand = brand
        self.name = name
        self.composition = composition
        self.needle_size = needle_size
        self.price = price
