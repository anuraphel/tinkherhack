import streamlit as st
from match_users import find_matches

st.title("💕 MIXIE MATCH 💕")

port = 8506
    
# User selects MBTI
user_mbti = st.selectbox("Select Your MBTI Type", ["INFJ", "ENFP", "INTP", "ENTP", "ISTJ", "ISFP", "ESFJ", "ENTJ"])

# Show matches
if st.button("Find Matches"):
    matches = find_matches(user_mbti)
      # Calls the function to find matches based on MBTI
    
    if matches:
        st.header("✨ Your Best Matches:")
    

        # Dictionary to store full details of each match for later display
        match_details = {}

        displayed_candidates = set()  # To track displayed candidates and avoid duplicates
        
        # Display all candidates' names with basic details
        for match in matches:
            if len(match) == 10:
                id, name, username, password, age, gender, location, mbti, interests, bio = match
                
                # Avoid displaying duplicate candidates
                if name not in displayed_candidates:
                    displayed_candidates.add(name)  # Add to the set of displayed candidates
                    
                    # Store the full details of each match
                    match_details[name] = {
                        "id": id,
                        "name": name,
                        "age": age,
                        "gender": gender,
                        "mbti": mbti,
                        "interests": interests,
                        "location": location,
                        "bio": bio,
                    }

                    # Display candidate's name as a clickable expander
                    with st.expander(f"👤 {name}"):
                        st.write(f"**Id**: {id}")
                        st.write(f"**Age**: {age}")
                        st.write(f"**Gender**: {gender}")
                        st.write(f"**MBTI**: {mbti}")
                        st.write(f"**Interests**: {interests}")
                        st.write(f"**Location**: {location}")
                        st.write(f"**Bio**: {bio}")
    
                        

        # If no matches are found, display a warning
        if not displayed_candidates:
            st.warning("❌ No matches found for your MBTI type.lalalal")
    else:
        st.warning("❌ No matches found for your MBTI type.")