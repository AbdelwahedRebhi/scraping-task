import pandas as pd
from scraper.Scraper import Scraper
from utils import export

data = pd.read_excel('billets.xlsx')

products = []
for item in data.index:
    scrap = Scraper(data['Brand'][item], data['Name'][item])
    available, product = scrap.start()
    if available:
        products.append(product)

export(products, "all")
