import pandas as pd
from database import Database, engine
from sqlalchemy.orm import sessionmaker
from models.Product import Product


def get_url(brand, product):
    brand = brand.strip().lower()
    product = product.lower().replace(' ', '-').replace("double-knit", "dk")
    url = f"https://www.wollplatz.de/wolle/{brand}/{brand}-{product}"

    return url


def export(data, type="all"):
    df = pd.DataFrame(data)
    print("\n")

    if type == "csv" or type == "all":
        df.to_csv("exports/products.csv", index=False,
                  sep=';', encoding='utf-8')
        print("Products exported to exports/products.csv")

    if type == "json" or type == "all":
        df.to_json("exports/products.json", orient="records")
        print("Products exported to exports/products.json")

    if type == "sqlite" or type == "all":
        Database.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        s = Session()
        for product in data:
            p = Product(**product)
            if s.query(Product).filter_by(name=p.name).first() is None:
                s.add(p)
        s.commit()
        print("Products exported to exports/products.db")
        s.close()
