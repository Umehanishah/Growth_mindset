import streamlit as st
from datetime import date

# Page Config
st.set_page_config(page_title="Age Calculator", page_icon="📅")
st.title("🎂 Age Calculator")

# User Input
st.header("Enter Your Birth Date")
day = st.number_input("Day", min_value=1, max_value=31, step=1)
month = st.number_input("Month", min_value=1, max_value=12, step=1)
year = st.number_input("Year", min_value=1900, max_value=date.today().year, step=1)

if st.button("Calculate Age"):
    try:
        birth_date = date(year, month, day)
        today = date.today()
        age_years = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        age_months = (today.month - birth_date.month) % 12
        age_days = (today - birth_date.replace(year=today.year)).days

        st.success(f"🎉 You are {age_years} years, {age_months} months, and {age_days} days old!")
    except ValueError:
        st.error("❌ Invalid date! Please enter a correct birth date.")

# Footer
st.write("---")
st.write("📌 Keep track of your age and cherish every moment!")
st.write("**Created by Hanishah**")
