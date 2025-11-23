import streamlit as st

def checkout_page(marble_baker):
    st.subheader("Checkout 🛒")
    password = st.text_input("Enter payment password:", type="password")

    if password == "123456":
        st.success("Password correct! Your order summary is below:")
        st.write("---")

        grand_total = 0
        empty_cart = True
        for category in ["Sweets", "Coffee", "Mojitos"]:
            items = marble_baker.get_items(category)
            for i, item in enumerate(items):
                qty = st.session_state.cart[category][i]
                if qty > 0:
                    st.write(f"{item.emoji} {item.name}: {qty} x JOD{item.price:.2f}")
                    grand_total += qty * item.price
                    empty_cart = False

        if empty_cart:
            st.warning("Your cart is empty. Please add items before checkout.")
            return

        st.write("---")
        st.subheader(f"Grand Total: JOD{grand_total:.2f}")

        payment_method = st.radio("Choose Payment Method:", ["Cash 💵", "Card 💳"])
        if st.button("Confirm Payment"):
            st.success(f"Payment completed successfully using {payment_method}!")
            st.balloons()
            st.write("Thank you for choosing **Marble Baker**! 🍰☕🍹")

    elif password != "":
        st.error("Wrong password! Try again.")

