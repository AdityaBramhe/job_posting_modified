# main.py

import sys
from process_jobs import process_jobs

def main():
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 50

    print(f"🚀 Running Agent 2 (Signal Processing) | Limit = {limit}")
    process_jobs(limit)
    print("✅ Agent 2 completed.")

if __name__ == "__main__":
    main()