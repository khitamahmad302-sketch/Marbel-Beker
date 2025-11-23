import streamlit as st
from PIL import Image
from bakery import Bakery
import home
import menu
import checkout

st.set_page_config(page_title="Marble Baker", layout="wide")



logo = Image.open("لوجو.png")


marble_baker = Bakery()

if "cart" not in st.session_state:
    st.session_state.cart = {
        "Sweets": [0]*len(marble_baker.sweets),
        "Coffee": [0]*len(marble_baker.coffees),
        "Mojitos": [0]*len(marble_baker.mojitos)
    }


st.sidebar.title("Marble Baker Menu 🍰☕🍹")
menu_option = st.sidebar.radio(
    "Go to:", ["Home 🏨", "Sweets 🍰", "Coffee ☕", "Mojitos 🍹", "Checkout 🛒"]
)


if menu_option == "Home 🏨":
    home.show_home(logo)
elif menu_option == "Sweets 🍰":
    menu.show_items_box("Sweets", marble_baker)
elif menu_option == "Coffee ☕":
    menu.show_items_box("Coffee", marble_baker)
elif menu_option == "Mojitos 🍹":
    menu.show_items_box("Mojitos", marble_baker)
elif menu_option == "Checkout 🛒":
    checkout.checkout_page(marble_baker)