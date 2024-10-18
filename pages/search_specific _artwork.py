"""
Yinshan Lin
CS 5001, Fall 2023
Final Project - Website for artworks

Website searches for a specific artwork
"""

import streamlit as st
from models.artworks import Artwork
from main import display_header, display_subheader, time_process


def input_name() -> str:
    """
    input specific artwork name
    """
    input_title = st.text_input('Enter the name of artwork: '
                                '(e.g. boy, Jew, panel)')
    return input_title


def split_artwork_title(artwork: object) -> list:
    """
    split artwork title into single lower words
    """
    # initialize artwork_title_nested_lst
    artwork_title_nested_lst = []
    artwork_title_lst = artwork.title
    for artwork_title in artwork_title_lst:
        # split artwork_title into single lower words
        artwork_title_split = artwork_title.lower().split(' ')
        artwork_title_nested_lst.append(artwork_title_split)
    return artwork_title_nested_lst


def search_artwork(
        title: str,
        artwork_title_nested_lst: str) -> list:
    """
    search for the input artwork and return result
    """
    # initialize num_lst
    num_lst = []
    for num in range(len(artwork_title_nested_lst)):
        artwork_title_lst = artwork_title_nested_lst[num]
        # check if input keywords are in artwork_title_lst
        if title.lower() in artwork_title_lst:
            num_lst.append(num)
    return num_lst


def display_image(num_lst: list, artwork: object):
    """
    image and info display function
    """
    # check if num_lst is None
    if num_lst != []:
        for num in num_lst:
            # assign to parallel list
            artwork_name = artwork.title[num]
            artwork_image = artwork.image[num]
            artwork_type = artwork.type[num]
            artwork_website = artwork.website[num]

            # display image
            st.image(artwork_image)
            # display info
            st.link_button(
                f':point_right: **{artwork_name}**', artwork_website
                )
            st.markdown(f'Type: {artwork_type}')

    # no result for searching
    else:
        st.markdown('No related artwork found.')


def main():
    """
    main function
    """
    # create a new Artwork Object
    artwork = Artwork()
    artwork.fetch()
    # page format
    display_header()
    display_subheader('Searching')
    # time progress bar
    time_process()
    # split all titles
    artwork_title_nested_lst = split_artwork_title(artwork)
    # input title
    input_title = input_name()
    if input_title:
        # search for the specific artwork
        num_lst = search_artwork(input_title, artwork_title_nested_lst)
        # display image
        display_image(num_lst, artwork)


if __name__ == '__main__':
    main()
