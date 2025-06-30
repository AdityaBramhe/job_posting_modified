import pandas as pd

def extract_signals(df):
    # --- Handle missing columns gracefully ---
    if 'description' not in df.columns:
        df['description'] = ""  # Fallback to empty string

    if 'department' not in df.columns:
        df['department'] = "Unknown"

    if 'tech_stack' not in df.columns:
        df['tech_stack'] = [[] for _ in range(len(df))]

    # --- Determine usable date column ---
    date_col = 'posting_date' if 'posting_date' in df.columns else (
        'scraped_date' if 'scraped_date' in df.columns else None
    )
    if date_col:
        df[date_col] = pd.to_datetime(df[date_col])
        df['posting_date'] = df[date_col]
    else:
        print("⚠️ No valid date column found. Using today's date as default.")
        df['posting_date'] = pd.Timestamp.now()

    # --- Urgency and Pain Point Detection ---
    df['is_urgent'] = df['description'].str.contains("immediate|ASAP|urgent", case=False, na=False)
    df['has_pain_points'] = df['description'].str.contains("legacy|migration|modernization", case=False, na=False)

    # --- Group by company + department ---
    grouped = df.groupby(['company', 'department']).agg({
        'description': 'count',
        'is_urgent': 'sum',
        'has_pain_points': 'sum',
        'tech_stack': lambda x: list(set([skill for sublist in x if isinstance(sublist, list) for skill in sublist]))
    }).reset_index()

    # --- Rename and filter scaling signals ---
    grouped = grouped.rename(columns={'description': 'role_count'})
    grouped = grouped[grouped['role_count'] >= 3]

    print(f"✅ Extracted {len(grouped)} signals.")
    return grouped
