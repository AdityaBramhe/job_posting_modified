import streamlit as st
import pandas as pd
from pymongo import MongoClient
from scripts.signal_rules import extract_signals
from scripts.summary_generator import generate_summaries

# --- Connect to MongoDB ---
MONGO_URI = "REMOVEDadityabramhe7:C3kg0TDi21QaKOAM@jobposting.tgcylyz.mongodb.net/"
client = MongoClient(MONGO_URI)
db = client["JobPosting"]
collection = db["ProcessedSignals"]

# --- Load Last 16 Processed Jobs ---
data = list(collection.find().sort([("_id", -1)]).limit(16))
df = pd.DataFrame(data)

st.title("📊 Job Intelligence Dashboard")

if df.empty:
    st.warning("No job posts found in MongoDB.")
else:
    # --- Apply Signal Rules ---
    signals_df = extract_signals(df)

    if not signals_df.empty:
        st.subheader("Top Hiring Signals")
        st.dataframe(signals_df)

        # --- Generate Summaries ---
        st.subheader("📝 Weekly Summaries")
        summaries = generate_summaries(signals_df)

        for s in summaries:
            st.markdown(f"✅ {s}")
    else:
        st.info("No scaling signals detected yet.")
