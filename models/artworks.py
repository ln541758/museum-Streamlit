"""
Yinshan Lin
CS 5001, Fall 2023
Final Project - Website for artworks

The file contains models of artworks in the Art Institute of Chicago
"""

import requests


class Artwork:
    """
    Artwork model
    """

    def __init__(self):
        """
        Constructor
        """
        self.image = []
        self.title = []
        self.website = []
        self.type = []

    def fetch(self):
        """
        fetches all artworks from the ARTIC API
        needs two fetches -- artwork data url & artwork info url
        """
        # limit number -- number of artwork you want to fetch from ARTIC
        limit_number = 100
        url = f'https://api.artic.edu/api/v1/artworks?limit={limit_number}'
        # try to fetch artwork data
        try:
            response = requests.get(url)
            # if artwork data url response
            if response.status_code == 200:
                data = response.json()
                for artwork in data['data']:
                    # get all artwork_image
                    image_id = artwork['image_id']
                    if image_id:
                        # construct artwork_image_url
                        artwork_image = (
                            f'https://www.artic.edu/iiif/2/{image_id}/full'
                            f'/843,/0/default.jpg'
                        )
                        # try to fetch artwork info
                        try:
                            image_response = requests.get(artwork_image)
                            # if artwork artwork_image_url response
                            if image_response.status_code == 200:
                                # get all artwork_image
                                self.image.append(artwork_image)

                                # get all artwork_title
                                artwork_title = artwork['title']
                                self.title.append(artwork_title)

                                # get all artwork_type
                                artwork_type = artwork['artwork_type_title']
                                self.type.append(artwork_type)

                                # get all artwork_id
                                artwork_id = artwork['id']

                                # get all specific_artwork_url
                                title_words = artwork_title.split()
                                title_join = '-'.join(title_words)
                                specific_artwork_url = (
                                    f'https://www.artic.edu/artworks/'
                                    f'{artwork_id}/{title_join}'
                                )
                                self.website.append(specific_artwork_url)
                            else:
                                print("Failed to fetch artworks info")
                        except requests.exceptions.ConnectionError:
                            print("Artworks info connection error occurred")
            else:
                print("Failed to fetch artworks data")
                return
        except requests.exceptions.ConnectionError:
            print("Artworks data connection error occurred")
            return
