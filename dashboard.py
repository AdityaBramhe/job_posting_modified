import streamlit as st
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from datetime import datetime

# MongoDB setup
mongo_url = "REMOVEDadityabramhe7:C3kg0TDi21QaKOAM@jobposting.tgcylyz.mongodb.net/"
client = MongoClient(mongo_url)
db = client["JobPosting"]
collection = db["ProcessedSignals"]

# Load data
@st.cache_data
def load_data():
    data = list(collection.find({}))
    return pd.DataFrame(data)

df = load_data()

st.title("📊 BD Signals Intelligence Dashboard")
st.markdown("Visualizing Agent 2 insights from job postings")

# Bar Chart: Top Hiring Companies
st.subheader("Top Hiring Companies")
top_companies = df['company'].value_counts().head(10)
st.bar_chart(top_companies)

# Pie Chart: Departments
st.subheader("Department Distribution")
department_counts = df['department'].value_counts()
fig1, ax1 = plt.subplots()
ax1.pie(department_counts, labels=department_counts.index, autopct='%1.1f%%')
ax1.axis("equal")
st.pyplot(fig1)

# Word Cloud: Tech Stack
st.subheader("Tech Stack Word Cloud")
all_tech = ', '.join([tech for sublist in df['tech_stack'] if isinstance(sublist, list) for tech in sublist])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_tech)
fig2, ax2 = plt.subplots()
ax2.imshow(wordcloud, interpolation='bilinear')
ax2.axis("off")
st.pyplot(fig2)

# Line Chart: Weekly Hiring Trends
st.subheader("Hiring Trend Over Time")
df['scraped_date'] = pd.to_datetime(df['scraped_date'])
weekly_trend = df.groupby(df['scraped_date'].dt.to_period("W")).size()
weekly_trend.index = weekly_trend.index.to_timestamp()
st.line_chart(weekly_trend)
