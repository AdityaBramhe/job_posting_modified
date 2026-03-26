# signal_rules.py

import pandas as pd
from collections import Counter


def extract_signals(df):
    if df.empty:
        print("⚠️ Empty DataFrame received.")
        return pd.DataFrame(), {}

    # --- Clean columns ---
    df['skills'] = df.get('skills', [[] for _ in range(len(df))])
    df['department'] = df.get('department', "Unknown")
    df['urgency'] = df.get('urgency', "Not urgent")

    # --- Convert urgency to numeric ---
    df['urgency_score'] = df['urgency'].apply(
        lambda x: 1 if str(x).lower() == "immediate" else 0
    )

    # --- Skill frequency ---
    all_skills = []
    for skills in df['skills']:
        if isinstance(skills, list):
            all_skills.extend(skills)

    skill_counts = dict(Counter(all_skills))

    # --- Hiring momentum (simple proxy) ---
    total_jobs = len(df)
    urgent_jobs = df['urgency_score'].sum()

    # momentum based on hiring volume + urgency
    momentum = (total_jobs * 0.7 + urgent_jobs * 0.3) / 100
    momentum = round(momentum, 2)

    # --- Grouping ---
    grouped = df.groupby(['company', 'department']).agg({
        'title': 'count',
        'urgency_score': 'mean'
    }).reset_index()

    grouped.rename(columns={
        'title': 'num_roles',
        'urgency_score': 'avg_urgency'
    }, inplace=True)

    grouped['hiring_momentum'] = round(momentum, 2)

    return grouped, skill_counts