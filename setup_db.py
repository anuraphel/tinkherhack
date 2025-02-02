import sqlite3

# Connect to SQLite3 database (creates file if not exists)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        location TEXT,
        mbti_type TEXT,
        interests TEXT,
        bio TEXT
    )
''')

# Insert dummy users
dummy_users = [
    ('Alice Johnson', 'alicej', 'pass123', 25, 'Female', 'New York', 'INFJ', 'Reading, Traveling, Yoga', 'Passionate about tech and books, looking for meaningful conversations.'),
('Michael Smith', 'michaels', 'securepass', 28, 'Male', 'Los Angeles', 'ENFP', 'Hiking, Movies, Cooking', 'Adventure seeker who loves deep talks and good food.'),
('Sophia Lee', 'sophial', 'mypassword', 23, 'Female', 'San Francisco', 'INTP', 'Painting, Music, Science Fiction', 'Creative soul who loves expressing through art and exploring ideas.'),
('Daniel Carter', 'danielc', 'danielpass', 30, 'Male', 'Chicago', 'ENTP', 'Startups, Chess, Stand-up Comedy', 'Always up for an intellectual debate or spontaneous adventure.'),
('Olivia Brown', 'oliviab', 'olivia321', 27, 'Female', 'Boston', 'ISTJ', 'Cooking, Reading, Fitness', 'A mix of discipline and fun, love deep conversations.'),
('James Wilson', 'jamesw', 'wilson123', 26, 'Male', 'Houston', 'ISFP', 'Photography, Travel, Designing', 'Love capturing moments and designing beautiful spaces.'),
('Emma Davis', 'emmad', 'emma321', 24, 'Female', 'Seattle', 'ESFJ', 'Volunteering, Teaching, Dancing', 'Passionate about education and making a difference.'),
('Liam Martinez', 'liamm', 'martinezpass', 29, 'Male', 'Austin', 'ENTJ', 'Gym, Cars, Leadership', 'Driven and goal-oriented, love meaningful conversations.'),
('Ava Thompson', 'avat', 'ava_pass', 22, 'Female', 'Miami', 'INFP', 'Poetry, Music, Deep Conversations', 'Empathetic and thoughtful, love understanding people.'),
('Ethan Hernandez', 'ethanh', 'ethanpass', 31, 'Male', 'San Diego', 'ENFJ', 'Debating, Writing, Networking', 'Driven by justice and making an impact in the world.')
]

cursor.executemany("INSERT INTO users (name,username,password, age, gender, location, mbti_type, interests, bio) VALUES (?,?,?, ?, ?, ?, ?, ?, ?)", dummy_users)

# Commit and close
conn.commit()
conn.close()

print("Database setup complete with dummy users!")
