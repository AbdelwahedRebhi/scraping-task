import pytest
from scraper.Scraper import Scraper


def test_valid_product():
    scrap = Scraper("Drops", "Paris")
    available, product = scrap.start()
    expected = {
        "brand": "Drops",
        "name": "Paris 1 Apricot",
        "composition": "100% Baumwolle",
        "needle_size": "5 mm",
        "price": "0,90"
    }
    assert available == True
    assert product == expected


def test_product_not_exists():
    scrap = Scraper("Adidas", "Shoes")
    available, product = scrap.start()
    assert available == False
    assert product == {}
