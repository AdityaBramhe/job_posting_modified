import kagglehub

# Download the dataset to a local path (e.g., ~/.cache/kagglehub)
path = kagglehub.dataset_download("ruchi798/data-science-job-salaries")

print("✅ Dataset downloaded successfully!")
print("📁 Path to dataset files:", path)
