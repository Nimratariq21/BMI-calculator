import streamlit as st

# Page Configuration
st.set_page_config(page_title="BMI Calculator", page_icon="😃", layout="centered")

# Simple CSS Styling
st.markdown(
    """
    <style>
        /* Center the content */
        .main {
            text-align: center;
        }

        /* Styling for input boxes */
        .stNumberInput > div {
            border-radius: 8px;
            border: 2px solid #3498db;
            padding: 8px;
        }

        /* Styled BMI result box */
        .bmi-box {
            background-color: blue;
            padding: 10px;
            border-radius: 8px;
            color: white;
            font-size: 22px;
            text-align: center;
            font-weight: bold;
            margin-top: 15px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# 🏋️ Title
st.title("💪 BMI Calculator 😃")

# Instructions
st.markdown("## 📝 Enter your **weight** and **height** please!")

# Input fields
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input("⚖️ Weight (kg):", min_value=1.0, format="%.2f")

with col2:
    height = st.number_input("📏 Height (m):", min_value=0.5, format="%.2f")

# Calculate BMI when inputs are valid
if height > 0 and weight > 0:
    bmi = weight / (height ** 2)  # BMI Formula
    st.markdown(f'<div class="bmi-box">🎯 your BMI is: {bmi:.2f} </div>', unsafe_allow_html=True)

    # BMI Categories
    if bmi < 18.5:
        st.warning("⚠️ Underweight – Eat well! 🍔")
    elif 18.5 <= bmi < 24.9:
        st.success("✅ Normal Weight – Perfect! 💪😎")
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ Overweight – Must do exercise! 🏃‍♂️")
    else:
        st.error("🚨 Obesity – Takecare of your health! 🏥🥗")

else:
    st.info("⚠️ Please enter a valid **weight and height** to calculate BMI. 😃")
