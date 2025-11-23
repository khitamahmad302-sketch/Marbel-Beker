import streamlit as st

def show_items_box(category: str, bakery):
    st.subheader(category)
    items = bakery.get_items(category)
    total = 0
    for i, item in enumerate(items):
        with st.container():
            st.markdown(f"**{item.emoji} {item.name}**")
            st.write(f"Price: JOD{item.price:.2f}")
            qty = st.number_input(
                "Quantity", min_value=0, value=st.session_state.cart[category][i], key=f"{category}_{i}"
            )
            st.session_state.cart[category][i] = qty
            total += qty * item.price
            st.write("---")
    st.write(f"**Total for {category}: JOD{total:.2f}**")

