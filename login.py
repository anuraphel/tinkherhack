import streamlit as st
import sqlite3

# Function to create a users table if it doesn't exist
def create_users_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS user
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      name TEXT, 
                      username TEXT UNIQUE, 
                      password TEXT)''')
    conn.commit()
    conn.close()

# Function to add a new user
def add_user(name, username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, username, password) VALUES (?, ?, ?)", 
                       (name, username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Function to verify user login
def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

# Create users table on app start
create_users_table()

# Set the title of the page
st.title("💕 Welcome to Mixie Match - Your Matchmaking App 💕")

# Tabs for Login and Sign-Up
tab1, tab2 = st.tabs(["🔑 Login", "📝 Sign Up"])

# ----------- LOGIN TAB -----------
with tab1:
    st.header("Login to Your Account")
    
    # Add a form for the user to log in
    with st.form(key="login_form"):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", placeholder="Enter your password", type="password")
        login_button = st.form_submit_button(label="Login")

    # Logic to check if the login is successful
    if login_button:
        user = authenticate_user(username, password)
        if user:
            st.success(f"Login Successful! Welcome, {user[1]} 🎉")
            st.markdown('<meta http-equiv="refresh" content="0; url= http://localhost:8506/">', unsafe_allow_html=True)
        else:
            st.error("Invalid username or password. Please try again.")

# ----------- SIGN-UP TAB -----------
with tab2:
    st.header("Create a New Account")

    # Add a sign-up form
    with st.form(key="signup_form"):
        name = st.text_input("Full Name", placeholder="Enter your full name")
        new_username = st.text_input("Username", placeholder="Choose a username")
        new_password = st.text_input("Password", placeholder="Create a password", type="password")
        confirm_password = st.text_input("Confirm Password", placeholder="Re-enter your password", type="password")
        signup_button = st.form_submit_button(label="Sign Up")

    # Logic for user registration
    if signup_button:
        if new_password != confirm_password:
            st.error("Passwords do not match! Please try again.")
        elif new_username and new_password and name:
            if add_user(name, new_username, new_password):
                st.success("Account created successfully! 🎉.")
                st.markdown('<meta http-equiv="refresh" content="0; url= http://localhost:8508/">', unsafe_allow_html=True)
            else:
                st.error("Username already taken. Try a different one.")
        else:
            st.error("Please fill out all fields.")

# Styling for buttons and inputs
st.markdown("""
    <style>
        .stTextInput>div>div>input {
            font-size: 18px;
            padding: 10px;
            border-radius: 5px;
        }
        .stButton>button {
            background-color: #FF5C8D;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #FF3B6F;
        }
    </style>
""", unsafe_allow_html=True)


