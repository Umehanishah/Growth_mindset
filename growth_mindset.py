import streamlit as st
from datetime import date

# Page Config
st.set_page_config(page_title="Age Calculator", page_icon="📅")
st.title("🎂 Age Calculator")

# User Input
st.header("Enter Your Birth Date")
birth_date = st.date_input("Select your birth date", min_value=date(1900, 1, 1), max_value=date.today())

if st.button("Calculate Age"):
    today = date.today()
    age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    age_months = (today.month - birth_date.month) % 12
    age_days = (today - birth_date.replace(year=today.year)).days

    st.success(f"🎉 You are {age_years} years, {age_months} months, and {age_days} days old!")

# Footer
st.write("---")
st.write("📌 Keep track of your age and cherish every moment!")
st.write("**Created by Hanishah**")
