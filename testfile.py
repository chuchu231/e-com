import streamlit as st

# Sample menu
dishes = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Fries": 2.99,
    "Soda": 1.99,
    "Ice Cream": 3.49
}

# Initialize session state for the cart
if "cart" not in st.session_state:
    st.session_state.cart = {}

# Horizontal menu bar using Streamlit buttons
st.markdown("""
    <style>
    .menu-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        background-color: #f8f9fa;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"
with col2:
    if st.button("🍽 Order"):
        st.session_state.page = "Order"
with col3:
    if st.button("🛒 Cart"):
        st.session_state.page = "Cart"

# Ensure page state is initialized
if "page" not in st.session_state:
    st.session_state.page = "Home"

st.title("🍔 Fast Food Order System")

if st.session_state.page == "Home":
    st.subheader("Welcome to our fast food ordering system!")
    st.write("Select 'Order' from the menu to start ordering.")

elif st.session_state.page == "Order":
    st.subheader("Select your favorite dishes:")
    
    # Display menu items
    for dish, price in dishes.items():
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**{dish}** - ${price:.2f}")
        with col2:
            qty = st.number_input(f"Quantity of {dish}", min_value=0, max_value=10, key=dish)
            if qty > 0:
                st.session_state.cart[dish] = qty
            elif dish in st.session_state.cart:
                del st.session_state.cart[dish]

elif st.session_state.page == "Cart":
    st.subheader("🛒 Your Cart")
    total_cost = 0
    if st.session_state.cart:
        for item, qty in st.session_state.cart.items():
            cost = dishes[item] * qty
            total_cost += cost
            st.write(f"{item} x {qty} = ${cost:.2f}")
        st.write(f"**Total: ${total_cost:.2f}**")
        if st.button("Place Order"):
            st.success("✅ Order placed successfully!")
            st.session_state.cart = {}  # Clear cart
    else:
        st.write("Your cart is empty.")