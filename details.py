import streamlit as st
import sqlite3

port = 8504

# Connect to SQLite3 database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Retrieve the username of the logged-in user
username = st.session_state.get("username", None)

# Page title
st.title("Fill in Your Details")

# Collecting additional user details
age = st.number_input("Age", min_value=18, max_value=100, step=1)
gender = st.text_input("Gender")
location = st.text_input("Location")
mbti_type = st.text_input("MBTI Type")
interest = st.text_input("Interest")
bio = st.text_input("Bio")

# When user clicks Submit button
if st.button("Submit"):
    if age and gender and location and mbti_type and interest and bio:
        # Updating the user's details in the database
        cursor.execute("""
        UPDATE users
        SET age = ?, gender = ?, location = ?, mbti_type = ?, interests = ?, bio = ?
        WHERE username = ?
        """, (age, gender, location, mbti_type, interest, bio, username))

        # Commit the transaction
        conn.commit()

        st.success("Details submitted successfully!")

        # Redirect to the homepage (or another page)
        st.markdown('<meta http-equiv="refresh" content="0; url= http://localhost:8506/">', unsafe_allow_html=True)
    else:
        st.error("Please fill in all fields.")

# Close the connection
conn.close()
