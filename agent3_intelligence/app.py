# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from scripts.mongo_loader import load_data
from scripts.signal_rules import extract_signals
from scripts.summary_generator import generate_summaries

st.set_page_config(page_title="Job Intelligence Dashboard", layout="wide")

st.title("🚀 Job Market Intelligence Dashboard")

# -------------------------------
# Load Data
# -------------------------------
df = load_data()

if df.empty:
    st.error("❌ No data found. Run Agent 1 & 2 first.")
    st.stop()

st.success(f"✅ Loaded {len(df)} job signals")

# -------------------------------
# Extract Signals
# -------------------------------
grouped_df, skill_counts = extract_signals(df)

# -------------------------------
# SECTION 1: Key Insights
# -------------------------------
st.header("📊 Key Insights")

summaries = generate_summaries(grouped_df, skill_counts)

for s in summaries[:5]:  # show top 5
    st.info(s)

# -------------------------------
# SECTION 2: Company Hiring Trends
# -------------------------------
st.header("🏢 Top Hiring Companies")

company_counts = df['company'].value_counts()

fig1, ax1 = plt.subplots()
company_counts.head(5).plot(kind='bar', ax=ax1)
ax1.set_ylabel("Number of Jobs")

st.pyplot(fig1)

# -------------------------------
# SECTION 3: Skill Demand
# -------------------------------
st.header("🧠 Top Skills in Demand")

if skill_counts:
    skill_df = pd.DataFrame(skill_counts.items(), columns=["Skill", "Count"])
    skill_df = skill_df.sort_values(by="Count", ascending=False)

    fig2, ax2 = plt.subplots()
    skill_df.head(5).plot(kind='bar', x='Skill', y='Count', ax=ax2)
    st.pyplot(fig2)
else:
    st.warning("No skill data available")

# -------------------------------
# SECTION 4: Department Distribution
# -------------------------------
st.header("🏢 Department Distribution")

dept_counts = df['department'].value_counts()

fig3, ax3 = plt.subplots()
dept_counts.plot(kind='pie', autopct='%1.1f%%', ax=ax3)

st.pyplot(fig3)

# -------------------------------
# SECTION 5: Urgency Analysis
# -------------------------------
st.header("🚨 Urgency Analysis")

urgency_counts = df['urgency'].value_counts()

fig4, ax4 = plt.subplots()
urgency_counts.plot(kind='bar', ax=ax4)

st.pyplot(fig4)

# -------------------------------
# SECTION 6: Raw Data (Optional)
# -------------------------------
st.header("📄 Raw Data Preview")

st.dataframe(df.head(20))