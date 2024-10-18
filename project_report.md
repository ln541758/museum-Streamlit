Yinshan Lin\
CS 5001, Fall 2023\
Project report for the final project

# 1. Project summary

This website features a comprehensive display of artworks, offering users options to view selected pieces in detail, browse by categories, search for specific artworks, and even encounter random pieces for surprise discovery. Additionally, it includes an online gift shop with art-inspired merchandise. Utilizing the 'Artwork' model connected to the ARTIC API, the site ensures an engaging experience for art enthusiasts.

# 2. Description of the REST API

## REST API: Art Institute of Chicago

**URL:** https://api.artic.edu/api/v1/artworks?limit=2

**Documentation:** https://api.artic.edu/docs/

**Description:** The ARTIC API provides JSON-formatted data as a REST-style service that allows me to fetch data about the museum’s public data to display artworks, including images, titles and types.

### Endpoints:
https://api.artic.edu/api/v1/artworks?limit={limit_number}
- fetch artworks data from the ARTIC API

## REST API: Gift Shops in Art Institute of Chicago

**URL:** https://api.artic.edu/api/v1/products?limit=2

**Documentation:** https://api.artic.edu/docs/#shop

**Description:** The ARTIC Shop API includes product images, titles, and prices in gift shop, which allows me to fetch data about the museum’s public data to display products in my website.

### Endpoints:
https://api.artic.edu/api/v1/products?limit={limit_number}
- fetch products from the ARTIC_SHOP API

# 3. List of features

## Feature: Highlight Artworks Demonstration

**Description:**
> It showcases highlighted artworks in a paginated format.
>
> Clicking the button enables browsing through pages back and forth.
>
> Clicking on the title of an artwork leads users to a page with comprehensive details about that specific piece, including its period, artist, and type.
>
> By clicking on the button near artwork images, users can view high-resolution versions, allowing for a closer look at the intricate details and craftsmanship of each piece.

**Model (data class):**
> 'Artwork'

**REST API endpoint:**
> https://api.artic.edu/api/v1/artworks?limit=2
>> *Note: {limit=2} is number of artwork you want to fetch from ARTIC*

**Pages:**
> 'main'

## Feature: Category-Based Browsing

**Description:**
> It offers a structured way to navigate the collection, enabling users to sort and view artworks based on its types. 
>
> Similarly, by clicking on the button near artwork images, users can view high-resolution versions, allowing for a closer look at the intricate details and craftsmanship of each piece.
>
> Also, clicking on the title of an artwork leads users to a page with comprehensive details about that specific piece, including its period, artist, and type.
>
> Additionally, selecting the number of artworks to view on a page empowers users to tailor their browsing experience according to their preferences.

**Model (data class):**
> 'Artwork'

**REST API endpoint:**
> https://api.artic.edu/api/v1/artworks?limit=2
>> *Note: {limit=2} is number of artwork you want to fetch from ARTIC*

**Pages:**
> 'category'

## Feature: Search for Specific Artwork

**Description:**
> User can search for specific artwork with their input. The website will return all the related artwork images, titles, types and official links.
>
> By clicking on the button near artwork images, users can view high-resolution versions, allowing for a closer look at the intricate details and craftsmanship of each piece.
>
> By clicking on the title of an artwork leads users to a page with comprehensive details about that specific piece, including its period, artist, and type.

**Model (data class):**
> 'Artwork'

**REST API endpoint:**
> https://api.artic.edu/api/v1/artworks?limit=2

**Pages:**
> 'search_specific_artwork'

## Feature: Genarate an artwork genarately

**Description:**
> This page provides users with a platform for aesthetic appreciation. Once the random button is clicked, accompanied by the drifting of balloons, the website will genarate an artwork randomly.
>
> Similarly, by clicking on the button near artwork images, users can view high-resolution versions, allowing for a closer look at the intricate details and craftsmanship of each piece.

**Model (data class):**
> 'Artwork'

**REST API endpoint:**
> https://api.artic.edu/api/v1/artworks?limit=2

**Pages:**
> 'artwork'

## Feature: Online Gift Shop

**Description:** 
> It includes an online gift shop showcasing a variety of merchandise inspired by the museum's artworks.
>
> By clicking on price tabs, users can view products within their desired price range.
>
> Similarly, by clicking on the button near artwork images, users can view high-resolution versions, allowing for a closer look at the intricate details and craftsmanship of each piece.

**Model (data class):** 
> Shop

**REST API endpoint:** 
> https://api.artic.edu/api/v1/products?limit=2'
>> *Note: {limit=2} is number of artwork you want to fetch from ARTIC*

**Pages:** 
> 'gift_shop'

# 4. Code highlights

Artworks are split based on the page number in session_state and displayed in two columns. The specific code is as follows:

```python
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
```

# 5. Next steps

- Implement greater interactivity between different features, such as adding a navigation bar to the main page to access various features.

- Integrate different search features, for example, under the 'search' category, include options like search by category, search by artwork, and search by input keywords.

- Enhance operational efficiency and reduce running time. \
\
My current runtime is quite long because I make a second call to the API to ensure the images are 100% valid. Thanks to the TA's advice, I tried using @cache, but it didn't significantly improve the speed. If I had more time, I would like to find out if there is a more efficient method. 

# 6. Reflection

This was my first time building a website with Python and Streamlit, and I felt a great sense of achievement when I saw the first image appear on the page. It was a breakthrough from zero to one, though looking back, I realize I might have been a little bit overly excited. Of course, there were challenges along the way. The Art Institute performed maintenance on their API and changed some parameters the day before my milestone submission, causing many images in my version 1.0 code to be uncallable. As a result, I made a second API call, sacrificing some running speed to ensure all images were valid. Next time I encounter such a situation, I will think more carefully about edge cases and manage my time better to avoid nearly missing the deadline.