import streamlit as st

def show_home(logo):
    st.image(logo, width=200)
    st.title("Marble Baker")
    st.markdown("""
    ### 🎀 Welcome to **Marble Baker**! 🎀

    Where delightful sweets meet aromatic coffee and refreshing mojitos.  
    Let our unique flavors tantalize your senses and make every moment with us truly sweet! 🍰☕🍹

    **⏰ Opening Hours:** 8:00 AM - 10:00 PM
    """)
