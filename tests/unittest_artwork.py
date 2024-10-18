"""
Yinshan Lin
CS 5001, Fall 2023
Final Project - Website for artworks

The file contains unittest for the model artwork
"""

from models.artworks import Artwork
from unittest.mock import Mock, patch
import unittest
import requests


class ArtworkTest(unittest.TestCase):
    def test_artwork_init(self):
        a = Artwork()
        self.assertEqual(a.image, [])
        self.assertEqual(a.title, [])
        self.assertEqual(a.website, [])
        self.assertEqual(a.type, [])

    def test_artwork_fetch_success(self):
        # good condition
        a = Artwork()
        with patch('artworks.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {
                'data': [
                    {'image_id': '00000123456789', 'title': 'title titles',
                     'id': '00000', 'artwork_type_title': 'artworktype'}]
            }
            a.fetch()
            self.assertEqual(
                a.image,
                ['https://www.artic.edu/iiif/2/00000123456789/full/843,/' +
                 '0/default.jpg'])
            self.assertEqual(a.title, ['title titles'])
            self.assertEqual(
                a.website,
                ['https://www.artic.edu/artworks/00000/title-titles'])
            self.assertEqual(a.type, ['artworktype'])

    def test_artwork_fetch_connection_error(self):
        # all url doesn't work
        a = Artwork()
        with patch('artworks.requests.get') as mock_get:
            mock_get.side_effect = requests.exceptions.ConnectionError()
            a.fetch()
            self.assertEqual(a.image, [])
            self.assertEqual(a.title, [])
            self.assertEqual(a.website, [])
            self.assertEqual(a.type, [])

    def test_artwork_fetch_bad_status_code(self):
        # all response.status_code != 200
        a = Artwork()
        with patch('artworks.requests.get') as mock_get:
            mock_get.return_value.status_code == 500
            a.fetch()
            self.assertEqual(a.image, [])
            self.assertEqual(a.title, [])
            self.assertEqual(a.website, [])
            self.assertEqual(a.type, [])

    def test_artwork_fetch_image_data_sccess_info_failure(self):
        # first time fetch sccess but second fetch fail
        # image_response.status_code != 200
        a = Artwork()
        with patch('artworks.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {
                'data': [
                    {'image_id': '00000123456789', 'title': 'title titles',
                     'id': '00000', 'artwork_type_title': 'artworktype'}]
            }

            failure_response = Mock(status_code=404)
            mock_get.side_effect = [mock_get.return_value, failure_response]

            a.fetch()
            self.assertEqual(a.image, [])
            self.assertEqual(a.title, [])
            self.assertEqual(a.website, [])
            self.assertEqual(a.type, [])

    def test_artwork_fetch_image_data_sccess_info_connection_error(self):
        # first time fetch sccess but second fetch raise ConnectionError
        a = Artwork()
        with patch('artworks.requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = {
                'data': [
                    {'image_id': '00000123456789', 'title': 'title titles',
                     'id': '00000', 'artwork_type_title': 'artworktype'}]
            }

            mock_get.side_effect = [
                mock_get.return_value, requests.exceptions.ConnectionError
                ]

            a.fetch()
            self.assertEqual(a.image, [])
            self.assertEqual(a.title, [])
            self.assertEqual(a.website, [])
            self.assertEqual(a.type, [])
