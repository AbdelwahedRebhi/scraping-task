import requests
from bs4 import BeautifulSoup
from utils import get_url


class Scraper:
    def __init__(self, brand, product):
        self.brand = brand.strip()
        self.product = product.strip()

        self.url = get_url(brand, product)
        page = requests.get(self.url)
        self.available = False

        if page.status_code != 404:
            print(f"Product {self.brand} {self.product} is found")
            self.available = True
            self.soup = BeautifulSoup(page.content, "html.parser")
        else:
            print(f"Product {self.brand} {self.product} is not found")

    def get_product_name(self):
        h1_name = self.soup.find("h1", {'id': "pageheadertitle"}).text

        if h1_name is not None:
            return h1_name[len(self.brand)+1:]

        return self.product

    def get_price(self):
        span_price = self.soup.find("span", {'class': "product-price"})

        if span_price is not None:
            return span_price.findChild("span", {"class": "product-price-amount"}).text

    def get_product_details(self):
        return self.soup.find("div", {'id': "pdetailTableSpecs"})

    def get_needle_size(self, product_details):
        td_needle = product_details.find(
            lambda tag: tag.name == "td" and "nadelstärke" in tag.text.lower())

        if td_needle is not None:
            return td_needle.find_next_sibling().text

    def get_composition(self, product_details):
        td_composition = product_details.find(
            lambda tag: tag.name == "td" and "zusammenstellung" in tag.text.lower())

        if td_composition is not None:
            return td_composition.find_next_sibling().text

    def start(self):
        if self.available:
            name = self.get_product_name()
            price = self.get_price()
            details = self.get_product_details()
            if details is not None:
                needle_size = self.get_needle_size(details)
                composition = self.get_composition(details)

            return self.available, {"brand": self.brand, "name": name, "composition": composition, "needle_size": needle_size, "price": price}

        return self.available, {}
