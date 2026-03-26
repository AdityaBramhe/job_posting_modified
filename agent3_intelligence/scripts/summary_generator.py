# summary_generator.py

def generate_summaries(df, skill_counts):
    summaries = []

    # 🔹 Top skill insight (global)
    if skill_counts:
        top_skill = max(skill_counts, key=skill_counts.get)
        top_skill_count = skill_counts[top_skill]
    else:
        top_skill = "Unknown"
        top_skill_count = 0

    for _, row in df.iterrows():
        company = row.get('company', 'Unknown')
        department = row.get('department', 'Unknown')
        roles = row.get('num_roles', 0)
        urgency = round(row.get('avg_urgency', 0), 2)
        momentum = round(row.get('hiring_momentum', 0), 2)

        # 🔥 Hiring intensity logic (better than before)
        if roles >= 15:
            hiring_scale = "large-scale expansion"
        elif roles >= 5:
            hiring_scale = "moderate hiring growth"
        else:
            hiring_scale = "limited hiring activity"

        # 🔥 Urgency interpretation
        if urgency > 0.5:
            urgency_text = "high urgency hiring"
        elif urgency > 0:
            urgency_text = "some urgent hiring signals"
        else:
            urgency_text = "no immediate urgency"

        # 🔥 Momentum interpretation
        if momentum > 0.6:
            momentum_text = "strong market momentum"
        elif momentum > 0.3:
            momentum_text = "stable growth trend"
        else:
            momentum_text = "slow or stable hiring market"

        # 🔥 FINAL BUSINESS-LEVEL SUMMARY
        summary = (
            f"{company} is undergoing {hiring_scale} in its {department} department "
            f"with {roles} active roles. "
            f"The hiring pattern shows {urgency_text}, "
            f"while overall signals indicate {momentum_text}. "
            f"Across the market, {top_skill.upper()} remains the most in-demand skill "
            f"with {top_skill_count} mentions."
        )

        summaries.append(summary)

    print("✅ Generated summaries.")
    return summaries