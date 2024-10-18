"""
Yinshan Lin
CS 5001, Fall 2023
Final Project - Website for artworks

Website randomly generates an artwork
"""

import random
import streamlit as st
from models.artworks import Artwork
from main import display_header, display_subheader, time_process


def random_artwork(artwork: object):
    """
    genarate a random artwork
    """
    # when the user clicks the button
    if st.button("Fetch random artwork"):
        artwork.fetch()
        # display the image
        num = random.randint(0, len(artwork.image))
        st.image(artwork.image[num], caption=f'Title: {artwork.title[num]}')


def main():
    """
    Main function
    """
    # create a new Artwork Object
    artwork = Artwork()
    # page format
    display_header()
    display_subheader('Artwork Appreciation')
    # time progress bar
    time_process()
    # display celebretory balloons
    st.balloons()
    # generate the random artwork
    random_artwork(artwork)


if __name__ == '__main__':
    main()
