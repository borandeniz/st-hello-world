import streamlit as st
from streamlit_elements import elements, mui, html, sync
from PIL import Image
import numpy as np

IMAGES = [
    "https://i.ibb.co/C9JXyjm/f3.jpg",
    "https://i.ibb.co/N6hyBxq/f4.jpg",
    "https://i.ibb.co/MhvCDR9/f5.jpg",
    "https://i.ibb.co/hV4J1ct/f2.jpg",
    "https://i.ibb.co/XVPdzP2/f1.jpg",
    "https://i.ibb.co/x1LPmwS/f6.jpg"
]


def slideshow_swipeable(images):
    # Generate a session state key based on images.
    key = f"slideshow_swipeable_{str(images).encode().hex()}"

    # Initialize the default slideshow index.
    if key not in st.session_state:
        st.session_state[key] = 0

    # Get the current slideshow index.
    index = st.session_state[key]

    # Create a new elements frame.
    with elements(f"frame_{key}"):

        # Use mui.Stack to vertically display the slideshow and the pagination centered.
        # https://mui.com/material-ui/react-stack/#usage
        with mui.Stack(spacing=2, alignItems="center"):

            # Create a swipeable view that updates st.session_state[key] thanks to sync().
            # It also sets the index so that changing the pagination (see below) will also
            # update the swipeable view.
            # https://mui.com/material-ui/react-tabs/#full-width
            # https://react-swipeable-views.com/demos/demos/
            with mui.SwipeableViews(index=index, resistance=True, onChangeIndex=sync(key)):
                for image in images:
                    html.img(src=image, css={"width": "50%", "display":"block", "margin-left": "auto", "margin-right": "auto"})

            # Create a handler for mui.Pagination.
            # https://mui.com/material-ui/react-pagination/#controlled-pagination
            def handle_change(event, value):
                # Pagination starts at 1, but our index starts at 0, explaining the '-1'.
                st.session_state[key] = value-1

            # Display the pagination.
            # As the index value can also be updated by the swipeable view, we explicitely
            # set the page value to index+1 (page value starts at 1).
            # https://mui.com/material-ui/react-pagination/#controlled-pagination
            mui.Pagination(page=index+1, count=len(images), color="primary", onChange=handle_change)


if __name__ == '__main__':
    
    # with st.expander('Some Screenshots From Our App'):
    #     tabs = st.tabs(list(np.array(range(1,11)).astype(str)))

    # for i in range(5):
    #     col1, col2, col3 = tabs[i].columns(3)
    #     with col1:
    #             st.write(' ')
    #     with col2:
    #             st.image(IMAGES[i])
    #     with col3:
    #             st.write(' ')
    
    # st.markdown("<h1 style='text-align: center; color: black;'>Fridgify</h1>", unsafe_allow_html=True)

    # st.markdown("<h2 style='text-align: center; color: black;'>Less Waste More Taste</h2>", unsafe_allow_html=True)
    
    image = Image.open('logo.png')

    st.image(image)

    st.markdown("<h4 style='text-align: center; color: black; font-weight: lighter;'>As Fridgify, we aim to reduce food waste by providing an intuitive and playful app that suggests recipes based on spare ingredients from users' fridges, making customized cooking easy and fun while reducing food waste and promoting sustainability.</h4>", unsafe_allow_html=True)
    
    # st.markdown("<style>a{text-align: center; color: black; font-weight: lighter;}</style>", unsafe_allow_html=True)
    
    url = 'https://www.figma.com/proto/5kvoTEoGkc2hp8UMAMnaSv/Yumm!-App?node-id=2167-639&scaling=scale-down&page-id=19%3A6&starting-point-node-id=2167%3A639'

    col1, col2, col3 = st.columns(3)

    with col1:
        pass
    with col2:
        st.markdown("<a href='https://www.figma.com/proto/5kvoTEoGkc2hp8UMAMnaSv/Yumm!-App?node-id=2167-639&scaling=scale-down&page-id=19%3A6&starting-point-node-id=2167%3A639'><h4 style='color: black;'>Check out the demo!</h4></a>", unsafe_allow_html=True)
    with col3:
        pass
    
    # st.markdown("<a href= 'https://www.figma.com/proto/5kvoTEoGkc2hp8UMAMnaSv/Yumm!-App?node-id=2167-639&scaling=scale-down&page-id=19%3A6&starting-point-node-id=2167%3A639'></a>", unsafe_allow_html=True)

    # st.title("Fridgify")

    # st.subheader("Less Waste More Taste")

    # st.write("Check out this link for the demo of our app! [link](https://www.figma.com/proto/5kvoTEoGkc2hp8UMAMnaSv/Yumm!-App?node-id=2167-639&scaling=scale-down&page-id=19%3A6&starting-point-node-id=2167%3A639)")

    # st.markdown("<h4 style='text-align: center; color: black; font-weight: lighter;'>Here are some screenshots from our app:</h4>", unsafe_allow_html=True)

    slideshow_swipeable(IMAGES)
