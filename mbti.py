import streamlit as st

port = 8508
# Expanded list of 25 questions, mapped to MBTI traits
questions = [
    {"question": "Do you feel energized by being around people?", "trait": "E"},
    {"question": "Do you enjoy working in a group rather than alone?", "trait": "E"},
    {"question": "Do you prefer concrete facts over abstract concepts?", "trait": "S"},
    {"question": "Do you trust your gut feelings more than logical reasoning?", "trait": "N"},
    {"question": "Do you prefer planning ahead rather than being spontaneous?", "trait": "J"},
    {"question": "Do you find social gatherings draining rather than energizing?", "trait": "I"},
    {"question": "Do you focus more on possibilities than reality?", "trait": "N"},
    {"question": "Do you make decisions based on logic rather than emotions?", "trait": "T"},
    {"question": "Do you like sticking to a schedule rather than going with the flow?", "trait": "J"},
    {"question": "Do you prefer deep one-on-one conversations over group discussions?", "trait": "I"},
    {"question": "Do you rely more on past experiences rather than future possibilities?", "trait": "S"},
    {"question": "Do you prioritize efficiency over people's feelings?", "trait": "T"},
    {"question": "Do you feel comfortable with last-minute changes?", "trait": "P"},
    {"question": "Do you prefer brainstorming over structured planning?", "trait": "N"},
    {"question": "Do you find it easy to approach new people?", "trait": "E"},
    {"question": "Do you enjoy solving practical problems over theoretical ones?", "trait": "S"},
    {"question": "Are you more driven by principles than personal values?", "trait": "T"},
    {"question": "Do you prefer a structured lifestyle over a flexible one?", "trait": "J"},
    {"question": "Do you enjoy small talk over deep conversations?", "trait": "E"},
    {"question": "Do you focus more on details than the big picture?", "trait": "S"},
    {"question": "Do you believe rules should always be followed?", "trait": "J"},
    {"question": "Do you enjoy exploring new ideas over following traditions?", "trait": "N"},
    {"question": "Do you tend to think critically rather than go with emotions?", "trait": "T"},
    {"question": "Do you find strict schedules limiting rather than helpful?", "trait": "P"},
]

# Function to display the MBTI test and collect answers
def get_mbti_result():
    if 'answers' not in st.session_state or st.button("Retake Test"):
        st.session_state.answers = {}

    for idx, q in enumerate(questions):
        answer = st.radio(q["question"], ["Yes", "No"], key=idx)
        st.session_state.answers[q["trait"]] = st.session_state.answers.get(q["trait"], 0) + (1 if answer == "Yes" else 0)

    if st.button('Submit'):
        mbti_type = determine_mbti_type(st.session_state.answers)
        st.write(f"### Your MBTI Type: **{mbti_type}**")
    if st.button("Next"):
            # Redirect to a premade external website after clicking "Next"
            
         st.markdown('<meta http-equiv="refresh" content="0; url= http://localhost:8504/">', unsafe_allow_html=True)

# Function to determine the MBTI type based on answers
def determine_mbti_type(answers):
    percentages = {trait: round((answers.get(trait, 0) / 6) * 100, 1) for trait in "EISNTFJP"}
    mbti_type = (
        "E" if percentages["E"] >= percentages["I"] else "I",
        "S" if percentages["S"] >= percentages["N"] else "N",
        "T" if percentages["T"] >= percentages["F"] else "F",
        "J" if percentages["J"] >= percentages["P"] else "P",
    )
    return "".join(mbti_type)
# Main function to run the app
def main():
    st.title('MBTI Personality Test')

    knows_mbti = st.radio("Do you already know your MBTI type?", ["Yes", "No"])

    if knows_mbti == "Yes":
        user_mbti = st.text_input("Enter your MBTI type (e.g., INFP, ESTJ):")
        if st.button("Next"):
            # Redirect to a premade external website after clicking "Next"
            st.markdown('<meta http-equiv="refresh" content="0; url=http://localhost:8504/">', unsafe_allow_html=True)
        if user_mbti:
            st.write(f"Your MBTI type is: {user_mbti}")
    else:
        get_mbti_result()

if __name__ == '__main__':
    main()
