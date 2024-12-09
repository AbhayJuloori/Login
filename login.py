import streamlit as st

# Simulated user authentication dictionary
users = {
    "admin": "abhay",
    "abhay": "abhay",
}

def authenticate(username, password):
    """Authenticate the user."""
    return users.get(username) == password

# Authentication form
st.title("Login Page")

menu = st.sidebar.selectbox("Menu", ["Login", "Register"])
if menu == "Login":
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            # Redirect to external link after login
            st.markdown(
                """<meta http-equiv="refresh" content="0; url=https://cloudassignmenthome.streamlit.app/">""",
                unsafe_allow_html=True,
            )
        else:
            st.error("Invalid username or password")

elif menu == "Register":
    st.subheader("Register")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Register"):
        if new_username and new_password:
            if new_username in users:
                st.error("Username already exists")
            else:
                users[new_username] = new_password
                st.success("Registration successful! You can now log in.")
        else:
            st.error("Please fill out both fields.")

# Display content to logged-in users
st.write("Use the menu on the left to navigate.")
