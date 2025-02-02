import sqlite3
import random

# Define MBTI compatibility chart
mbti_compatibility = {
    "INFJ": ["ENFP", "ENTP", "ENFJ", "INTJ"],
    "ENFP": ["INFJ", "INTJ", "ENTJ", "INFP"],
    "INTP": ["ENTP", "INTJ", "ENTJ", "INFJ"],
    "ENTP": ["INFJ", "INTP", "INTJ", "ENFJ"],
    "ISTJ": ["ESTP", "ESFJ", "ISFJ", "ISTP"],
    "ESTP": ["ISTJ", "ISFJ", "ESFJ", "ISTP"],
    "ISFJ": ["ESFP", "ESTP", "ISFP", "ISTJ"],
    "ESFJ": ["ISTJ", "ISFJ", "ESTP", "ESFP"],
    "INTJ": ["ENFP", "ENTP", "INTP", "INFJ"],
    "ENTJ": ["INFP", "ENFP", "INTP", "INTJ"],
    "INFP": ["ENFJ", "ENTJ", "ENFP", "INFJ"],
    "ENFJ": ["INFP", "INFJ", "ENFP", "INTP"],
    "ISTP": ["ESTJ", "ESFP", "ISTJ", "ISFP"],
    "ESTJ": ["ISTP", "ISFP", "ESFP", "ESTP"],
    "ISFP": ["ESFJ", "ESTJ", "ISFJ", "ISTP"],
    "ESFP": ["ISFJ", "ISTP", "ESFJ", "ESTJ"]
}

# Function to find matches for the given user's MBTI
def find_matches(user_mbti):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Get compatible types for the user
    compatible_types = mbti_compatibility.get(user_mbti, [])
    print(f"Compatible types for {user_mbti}: {compatible_types}")
    if not compatible_types:
        print(f"No compatible types found for {user_mbti}.")
        return []  # Return empty list if no compatible types found

    # Query database for matching users
    query = "SELECT * FROM users WHERE mbti_type IN ({})".format(",".join(["?"] * len(compatible_types)))
    print(f"Executing query: {query} with {compatible_types}")
    
    try:
        cursor.execute(query, compatible_types)
        matches = cursor.fetchall()
        print(f"Found matches: {matches}")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        matches = []

    conn.close()

    return matches[:5]

# Function to add sample users to the database (for testing)
def add_sample_users():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Create the users table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        mbti_type TEXT
    )''')

    # Add some sample users
    cursor.execute("INSERT INTO users (name, mbti_type) VALUES (?, ?)", ("Alice", "ENFP"))
    cursor.execute("INSERT INTO users (name, mbti_type) VALUES (?, ?)", ("Bob", "INFJ"))
    cursor.execute("INSERT INTO users (name, mbti_type) VALUES (?, ?)", ("Charlie", "INTJ"))
    cursor.execute("INSERT INTO users (name, mbti_type) VALUES (?, ?)", ("David", "ENFP"))
    cursor.execute("INSERT INTO users (name, mbti_type) VALUES (?, ?)", ("Eve", "INFJ"))
    
    conn.commit()

    # Verify users are added
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("Users in the database:", users)

    conn.close()

# Example usage:
if __name__ == "__main__":
    # First, add some sample users to the database
    add_sample_users()

    # Now, try finding matches for a user
    user_mbti = "ENFP"  # Example MBTI type
    matches = find_matches(user_mbti)
    print(f"Top matches for {user_mbti}: {matches}")
