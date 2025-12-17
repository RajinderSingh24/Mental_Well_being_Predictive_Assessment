import pickle
import streamlit as st
import pandas as pd

model = pickle.load(open("knn_model.pkl", "rb"))

st.title("Mental Well-Being Prediction System")
st.write("Enter your lifestyle details to get a prediction and feedback.")
age = st.number_input("What is your age?", min_value=1, max_value=100, value=21)

sleep_hours = st.selectbox(
    "How many hours do you usually sleep in a day?",
    [1,2,3,4,5,6,7,8,9,10]
)

screen_time_hours = st.selectbox(
    "How many hours do you use a mobile, laptop or television in a day?",
    [1,2,3,4,5,6,7,8]
)

water_intake = st.selectbox(
    "How many liters of water do you drink in a day?",
    [1,2,3,4,5,6]
)

exercise = st.selectbox(
    "How often do you exercise in a week?",
    [
        "I do not exercise at all",
        "I exercise 1 to 2 days a week",
        "I exercise 3 to 5 days a week",
        "I exercise almost every day"
    ]
)

work_study_hours = st.selectbox(
    "How many hours do you work or study in a day?",
    [0,1,2,3,4,5,6,7,8]
)

breaks = st.selectbox(
    "How often do you take breaks while working or studying?",
    ["Rarely","Sometimes","Often"]
)

multitasking = st.selectbox(
    "Do you usually do many tasks at the same time?",
    ["Yes","No"]
)

stress_level = st.selectbox(
    "How stressed do you feel on most days?",
    [1,2,3,4,5]
)

social_time_hours = st.selectbox(
    "How much time do you spend talking to friends or family in a day?",
    [1,2,3,4,5,6]
)

relationship = st.selectbox(
    "How would you describe your relationship with your family and friends?",
    ["Poor","Average","Good","Excellent"]
)

hobbies = st.selectbox(
    "Do you spend time doing hobbies or activities you enjoy?",
    ["Yes","No"]
)

exercise_map = {
    "I do not exercise at all": 0,
    "I exercise 1 to 2 days a week": 1,
    "I exercise 3 to 5 days a week": 2,
    "I exercise almost every day": 3
}

break_map = {"Rarely": 1, "Sometimes": 2, "Often": 0}

multitasking_val = 1 if multitasking == "Yes" else 0

relationship_map = {
    "Poor": 3,
    "Average": 0,
    "Good": 2,
    "Excellent": 1
}

hobbies_val = 1 if hobbies == "Yes" else 0

user_input = pd.DataFrame([{
    "age": age,
    "sleep_hours": sleep_hours,
    "screen_time_hours": screen_time_hours,
    "water_intake": water_intake,
    "exercise_frequency": exercise_map[exercise],
    "work_study_hours": work_study_hours,
    "break_frequency": break_map[breaks],
    "multitasking": multitasking_val,
    "stress_level": stress_level,
    "social_time_hours": social_time_hours,
    "relationship_quality": relationship_map[relationship],
    "hobbies": hobbies_val
}])

if st.button("Predict Mental Well-Being"):
    prediction = model.predict(user_input)[0]

    if prediction == 2:
        result = "Psychological Strain"
    elif prediction == 0:
        result = "Adaptive Coping"
    else:
        result = "Psychological Flourishing"

    st.subheader("Prediction Result")
    st.success(result)

    def generate_feedback(data):
        feedback = []

        if data["stress_level"] >= 3:
            feedback.append(
                "Your stress level is high. Try relaxation techniques or take regular breaks."
            )

        if data["sleep_hours"] < 6:
            feedback.append(
                "Your sleep duration is low. Aim for 7–8 hours of sleep daily."
            )

        if data["screen_time_hours"] > 4:
            feedback.append(
                "High screen time can affect mental well-being. Consider reducing screen usage."
            )

        if data["social_time_hours"] < 3:
            feedback.append(
                "Spending more time with friends or family can improve emotional well-being."
            )

        if data["exercise_frequency"] <= 1:
            feedback.append(
                "Regular physical activity can positively impact mental well being and improve mood."
            )

        if not feedback:
            feedback.append(
                "Your lifestyle habits look balanced. Keep maintaining them."
            )

        return feedback

    st.subheader("Personalized Feedback")

    feedback = generate_feedback(user_input.iloc[0])

    for tip in feedback:
        st.write("•", tip)
