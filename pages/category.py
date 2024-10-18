"""
Yinshan Lin
CS 5001, Fall 2023
Final Project - Website for artworks

Website shows corresponding artworks by category and num_control
"""

import streamlit as st
from models.artworks import Artwork
from main import display_header, display_subheader, time_process


def get_images_by_category(category: str, artwork: object) -> list:
    """
    return the corresponding index lists by the selected category
    """
    # initialize type_idx
    type_idx = []
    for num in range(len(artwork.type)):
        type = artwork.type[num]
        # find the same category
        if category.lower() == type.lower():
            type_idx.append(num)
    return type_idx


def selectbox_radio() -> tuple[str, int]:
    """
    category selectbox function
    """
    # set up two columns as category filters
    col_selectbox, space, col_radio = st.columns([1.2, 0.5, 1])

    # left column -- selectbox
    with col_selectbox:
        option = st.selectbox(
            ":mag_right: Choose the type of artwork",
            ('Print', 'Photograph', 'Drawing and Watercolor', 'Textile',
             'Painting', 'Vessel', 'Book')
        )
        # add empty line
        st.markdown('\n')
        st.markdown(f':grey[You selected: *{option}*]')

    # right column -- radio
    with col_radio:
        max_artwork = st.radio(
            "Select the number of artworks",
            ['0-5', '6-20', '21-50'], horizontal=True
        )
    # get max_artwork number
    max_artwork = int(max_artwork.split('-')[1])
    return option, max_artwork


def display_image(max_artwork: int, type_idx: list, artwork: object):
    """
    display image function
    """
    # initialize the number of display images
    display_images = 0
    # display images as two columns
    col_left, col_right = st.columns(2, gap='large')

    for num in range(0, min(len(type_idx), max_artwork), 2):
        # combine two columns as a whole and then iterate
        if display_images % 2 == 0:    # left column
            idx = type_idx[num]
            image = artwork.image[idx]
            title = f':point_right: {artwork.title[idx]}'
            col_left.image(image, use_column_width=True)
            col_left.link_button(f'**{title}**', artwork.website[idx])
            display_images += 1
            # right column
            if num + 1 < len(type_idx) and display_images < max_artwork:
                idx_next = type_idx[num + 1]
                image_next = artwork.image[idx_next]
                title_next = f':point_right: {artwork.title[idx_next]}'
                col_right.image(image_next, use_column_width=True)
                col_right.link_button(f'**{title_next}**',
                                      artwork.website[idx_next])
                display_images += 1


def main():
    """
    main function
    """
    # create a new Artwork Object
    artwork = Artwork()
    artwork.fetch()
    # page format
    display_header()
    display_subheader('Category')
    # time progress bar
    time_process()
    # get selectbox_option and max_artwork in page
    option, max_artwork = selectbox_radio()
    # get type_idx
    type_idx = get_images_by_category(option, artwork)
    # display the image and title
    display_image(max_artwork, type_idx, artwork)


if __name__ == '__main__':
    main()
