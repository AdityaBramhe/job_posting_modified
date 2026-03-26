# main.py

from scripts.mongo_loader import load_data
from scripts.signal_rules import extract_signals
from scripts.summary_generator import generate_summaries
import os

if __name__ == "__main__":

    df = load_data()

    if df.empty:
        print("⚠️ No data found in MongoDB.")
        exit()

    print("✅ Loaded data:", df.shape)

    # 🔥 Extract signals
    grouped_df, skill_counts = extract_signals(df)

    print("\n📊 Grouped Signals:\n", grouped_df.head())

    # 🔥 Generate summaries
    summaries = generate_summaries(grouped_df, skill_counts)

    print(f"\n🧾 Total summaries: {len(summaries)}\n")

    for s in summaries:
        print(f"--- Summary ---\n{s}\n")

    # Save output
    os.makedirs("data", exist_ok=True)
    with open("data/weekly_summaries.txt", "w") as f:
        for s in summaries:
            f.write(s + "\n\n")

    print("✅ Agent 3 complete. Summaries saved.")