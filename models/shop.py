"""
Yinshan Lin
CS 5001, Fall 2023
Final Project - Website for artworks

The file contains models of products in the gift shop of ARTIC
"""

import requests


class Shop:
    """
    Shop model
    """

    def __init__(self):
        """
        Constructor
        """
        self.image = []
        self.title = []
        self.price = []

    def fetch(self):
        """
        fetches all products from the ARTIC_SHOP API
        needs two fetches -- product data url & product info url
        """
        # limit number -- number of products you want to fetch from ARTIC_SHOP
        limit_number = 35
        url = f'https://api.artic.edu/api/v1/products?limit={limit_number}'
        try:
            response = requests.get(url)
            # if product data url response
            if response.status_code == 200:
                data = response.json()
                for product in data['data']:
                    # get all product_image_url
                    product_image = product['image_url']
                    # try to fetch product info
                    try:
                        image_response = requests.get(product_image)
                        # if artwork artwork_image_url response
                        if image_response.status_code == 200:
                            # get all product_image
                            self.image.append(product_image)

                            # get all product_title
                            product_title = product['title']
                            self.title.append(product_title)

                            # get all product_price
                            product_price = product['max_current_price']
                            self.price.append(product_price)
                        else:
                            print("Failed to fetch products info in gift shop")
                    except requests.exceptions.ConnectionError:
                        print("Products info connection error occurred")
            else:
                print("Failed to fetch products data in gift shop")
                return
        except requests.exceptions.ConnectionError:
            print("Products data connection error occurred")
            return
