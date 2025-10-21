import streamlit as st
import pandas as pd

st.set_page_config(page_title="Earnings Estimator", layout="centered")

st.title("💰 Earnings Estimator")
st.markdown("Founder-grade clarity on potential income based on role, location, and experience.")

# --- Input Panel ---
industry = st.selectbox("Industry", ["Technology", "Finance", "Healthcare", "Education", "Consulting", "Other"])
role = st.text_input("Role Title", placeholder="e.g. Product Manager, Data Analyst")
location = st.selectbox("Location", ["USA", "UK", "Germany", "India", "Remote", "Other"])
experience = st.slider("Years of Experience", 0, 30, 5)
work_type = st.radio("Work Type", ["Full-time", "Freelance", "Contract"])
education = st.selectbox("Education Level", ["High School", "Bachelor's", "Master's", "PhD"])

# --- Base Rates (simplified model) ---
base_salaries = {
    "Technology": 70000,
    "Finance": 65000,
    "Healthcare": 60000,
    "Education": 45000,
    "Consulting": 55000,
    "Other": 50000
}

location_multiplier = {
    "USA": 1.2,
    "UK": 1.1,
    "Germany": 1.05,
    "India": 0.6,
    "Remote": 1.0,
    "Other": 0.9
}

education_bonus = {
    "High School": 0,
    "Bachelor's": 5000,
    "Master's": 10000,
    "PhD": 15000
}

work_type_multiplier = {
    "Full-time": 1.0,
    "Freelance": 1.3,
    "Contract": 1.1
}

# --- Earnings Calculation ---
base = base_salaries.get(industry, 50000)
location_factor = location_multiplier.get(location, 1.0)
edu_bonus = education_bonus.get(education, 0)
type_factor = work_type_multiplier.get(work_type, 1.0)

estimated_earnings = (base + (experience * 2000) + edu_bonus) * location_factor * type_factor

# --- Output ---
st.subheader("📊 Estimated Annual Earnings")
st.metric(label="Estimated Earnings", value=f"${estimated_earnings:,.0f}")

st.caption("This estimate is based on simplified assumptions. For investor-grade modeling, contact directly.")
