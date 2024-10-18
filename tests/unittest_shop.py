"""
Yinshan Lin
CS 5001, Fall 2023
Final Project - Website for artworks

The file contains unittest for the model shop
"""

from models.shop import Shop
from unittest.mock import Mock, patch
import unittest
import requests


class ShopTest(unittest.TestCase):
    def test_shop_init(self):
        s = Shop()
        self.assertEqual(s.image, [])
        self.assertEqual(s.title, [])
        self.assertEqual(s.price, [])

    def test_shop_fetch_success(self):
        s = Shop()
        with patch('shop.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {
                'data': [
                    {'image_url': 'product.jpg', 'title': 'titles',
                     'max_current_price': 'price'}]
            }
            s.fetch()
            self.assertEqual(s.image, ['product.jpg'])
            self.assertEqual(s.title, ['titles'])
            self.assertEqual(s.price, ['price'])

    def test_shop_fetch_connection_error(self):
        s = Shop()
        with patch('shop.requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.ConnectionError()
            s.fetch()
            self.assertEqual(s.image, [])
            self.assertEqual(s.title, [])
            self.assertEqual(s.price, [])

    def test_shop_fetch_bad_status_code(self):
        s = Shop()
        with patch('shop.requests.get') as mock_get:
            mock_get.return_value.status_code = 500
            s.fetch()
            self.assertEqual(s.image, [])
            self.assertEqual(s.title, [])
            self.assertEqual(s.price, [])

    def test_artwork_fetch_image_data_sccess_info_failure(self):
        s = Shop()
        with patch('shop.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {
                'data': [
                    {'image_url': 'product.jpg', 'title': 'titles',
                     'max_current_price': 'price'}]
            }

            failure_response = Mock(status_code=404)
            mock_get.side_effect = [mock_get.return_value, failure_response]

            s.fetch()
            self.assertEqual(s.image, [])
            self.assertEqual(s.title, [])
            self.assertEqual(s.price, [])

    def test_artwork_fetch_image_data_sccess_info_connection_error(self):
        s = Shop()
        with patch('shop.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {
                'data': [
                    {'image_url': 'product.jpg', 'title': 'titles',
                     'max_current_price': 'price'}]
            }

            mock_get.side_effect = [
                mock_get.return_value, requests.exceptions.ConnectionError
                ]

            s.fetch()
            self.assertEqual(s.image, [])
            self.assertEqual(s.title, [])
            self.assertEqual(s.price, [])
