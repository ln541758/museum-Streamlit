"""
Yinshan Lin
CS 5001, Fall 2023
Final Project - Website for artworks

Website shows online gift shop of the Art Institute of Chicago
"""

import streamlit as st
from models.shop import Shop
from main import display_header, time_process, display_subheader


def seperate_index_to_tags(shop: object) -> list:
    """
    get index_list for different tags
    """
    # initialize lst_idx of tabs
    cheap_lst_idx = []
    medium_lst_idx = []
    expen_lst_idx = []
    super_expen_lst_idx = []

    # distribute idx by tag condition
    for num in range(len(shop.price)):
        price = shop.price[num]
        if price <= 20:
            cheap_lst_idx.append(num)
        elif price <= 50:
            medium_lst_idx.append(num)
        elif price <= 100:
            expen_lst_idx.append(num)
        else:
            super_expen_lst_idx.append(num)

    # set up price_lst_idx as parallel list
    price_lst_idx = [
        cheap_lst_idx,
        medium_lst_idx,
        expen_lst_idx,
        super_expen_lst_idx
        ]
    return price_lst_idx


def page_layout(lst_idx: list, shop: object):
    """
    two columns layout for products
    """
    # initialize display_images
    display_images = 0
    # display images as two columns
    col_left, space, col_right = st.columns([1, 0.3, 1])

    for num in range(0, len(lst_idx), 2):
        # combine two columns as a whole and then iterate
        with col_left:      # left column
            if display_images <= len(lst_idx):
                idx = lst_idx[num]
                st.image(shop.image[idx], use_column_width=True)
                st.markdown(f'**{shop.title[idx]}**')
                st.markdown(f'${shop.price[idx]}')
                st.markdown('\n')
                display_images += 1
        with col_right:     # right column
            if (num + 1 < len(lst_idx) and
                    display_images < len(lst_idx)):
                idx = lst_idx[num + 1]
                st.image(shop.image[idx], use_column_width=True)
                st.markdown(f'**{shop.title[idx]}**')
                st.markdown(f'${shop.price[idx]}')
                st.markdown('\n')
                display_images += 1


def display_gift(price_lst_idx: list, shop: object):
    """
    display gift images and details
    """

    # set up tabs by prices
    tab_cheap, tab_medium, tab_expen, tab_super_expen = st.tabs(
        ['          $1 - $20        ',
         '          $21 - $50        ',
         '          $50 - $100        ',
         '          $100 -            ']
        )
    tabs = [tab_cheap, tab_medium, tab_expen, tab_super_expen]

    # iterate images in different tabs
    for num in range(len(tabs)):
        tab = tabs[num]
        lst_idx = price_lst_idx[num]
        with tab:
            # display images
            page_layout(lst_idx, shop)


def main():
    """
    Main function
    """
    # create a new Artwork Object
    shop = Shop()
    shop.fetch()
    # page format
    display_header()
    display_subheader('Online Gift Shop :shopping_bags:')
    # time progress bar
    time_process()
    # get index_list for different tags
    price_lst_idx = seperate_index_to_tags(shop)
    # display products
    display_gift(price_lst_idx, shop)


if __name__ == '__main__':
    main()
