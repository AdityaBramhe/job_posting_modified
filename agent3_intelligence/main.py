from scripts.mongo_loader import load_data
from scripts.signal_rules import extract_signals
from scripts.summary_generator import generate_summaries

if __name__ == "__main__":
    df = load_data(limit=16)  # ✅ Access last 16 processed jobs
    signals_df = extract_signals(df)
    summaries = generate_summaries(signals_df)

    # Save summaries for dashboard or email
    with open("data/weekly_summaries.txt", "w") as f:
        for s in summaries:
            f.write(s + "\n\n")

    print("✅ Intelligence Agent MVP complete. Summaries ready in /data folder.")
