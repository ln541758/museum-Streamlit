"""
Yinshan Lin
CS 5001, Fall 2023
Final Project - Website for artworks

Main Page of the website which demonstrates highlights
"""

import streamlit as st
import time
from models.artworks import Artwork


def display_header():
    """
    header display function
    """
    # add header
    st.header(':red[ART INSTITUTE OF CHICAGO] :classical_building:')
    # add divider
    st.divider()


def display_subheader(subheader: str):
    """
    subheader display function
    """
    # add subheader
    st.subheader(subheader)
    # add empty line
    st.markdown('\n')


def time_process():
    """
    progress bar display function
    """
    # initialize time bar
    bar = st.progress(0)
    # update the bar
    for percent_complete in range(100):
        time.sleep(0.04)
        bar.progress(percent_complete + 1)
    # clear bar
    bar.empty()


def initialize_session_state():
    """
    initialize values in session_state
    """
    if 'page_number' not in st.session_state:
        st.session_state.page_number = 1


def calcualte_page_number(image_per_page: int, artwork: object) -> int:
    """
    calculate page_number based on image_per_page
    """
    # add one page
    if len(artwork.image) % image_per_page > 0:
        page_number = len(artwork.image) // image_per_page + 1
    # don't need to add pages
    else:
        page_number = len(artwork.image) // image_per_page
    return page_number


def display_page_button(page_number: int):
    """
    page button display function
    """
    # add buttons as columns
    col_previous, space1, col_page_number, space2, col_next = st.columns(
        [1, 1.8, 1, 1.8, 1])
    # left button
    with col_previous:
        if st.button('Previous'):
            if st.session_state.page_number > 1:
                st.session_state.page_number -= 1
    # right button
    with col_next:
        if st.button('Next'):
            if st.session_state.page_number < page_number:
                st.session_state.page_number += 1
    # middle button
    with col_page_number:
        st.markdown(f'{st.session_state.page_number}/{page_number}')


def split_image(image_per_page: int) -> int:
    """
    split image by image_per_page
    """
    start_image = (st.session_state.page_number - 1) * image_per_page
    end_image = start_image + image_per_page
    return start_image, end_image


def display_image(start_image: int, end_image: int, artwork: object):
    """
    image display function
    """
    # adjust formatting - add empty lines
    st.markdown('\n')
    st.markdown('\n')
    st.markdown('\n')

    # display images as two columns
    col_left, col_right = st.columns(2, gap='large')
    for num in range(start_image, min(end_image, len(artwork.image)), 2):
        # get image and title
        image = artwork.image[num]
        title = f':point_right: {artwork.title[num]}'
        # combine two columns as a whole and then iterate
        # left column
        col_left.image(image, use_column_width=True)
        col_left.link_button(f'**{title}**', artwork.website[num])
        if num + 1 < len(artwork.image):    # right column
            image_next = artwork.image[num + 1]
            title_next = f':point_right: {artwork.title[num + 1]}'
            col_right.image(image_next, use_column_width=True)
            col_right.link_button(f'**{title_next}**',
                                  artwork.website[num + 1])
        # add empty line
        st.markdown('\n')


def main():
    """
    main function
    """
    # create a new Artwork Object
    artwork = Artwork()
    artwork.fetch()
    # page format
    display_header()
    display_subheader('Highlights')
    # time progress bar
    time_process()
    # initialize values in session_state
    initialize_session_state()
    # initialize image_per_page
    image_per_page = 6
    # get page_number
    page_number = calcualte_page_number(image_per_page, artwork)
    # display page button
    display_page_button(page_number)
    # get the start_image and end_image of current page
    start_image, end_image = split_image(image_per_page)
    # display all images
    display_image(start_image, end_image, artwork)


if __name__ == '__main__':
    main()
