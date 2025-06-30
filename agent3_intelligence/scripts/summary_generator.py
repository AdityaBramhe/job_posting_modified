from transformers import pipeline
from jinja2 import Template
import os

def load_template():
    template_path = os.path.join(os.path.dirname(__file__), "..", "templates", "summary_template.txt")
    with open("templates/summary_template.txt", "r") as f:
        return Template(f.read())

def generate_summaries(df, use_llm=True):
    template = load_template()
    summaries = []

    summarizer = None
    if use_llm:
        try:
            # ✅ Use an open-access summarization model
            summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
            print("✅ LLM summarizer loaded.")
        except Exception as e:
            print(f"⚠️ Failed to load LLM: {e}")
            use_llm = False

    for _, row in df.iterrows():
        
        tech_stack_str = ", ".join(row.get('tech_stack', [])) if isinstance(row.get('tech_stack', []), list) else "N/A"
        # Fill the Jinja template with job details
        filled = template.render(
            company=row.get('company', 'Unknown'),
            department=row.get('department', 'Unknown'),
            count=row.get('role_count', 0),
            urgent="Yes" if row.get('is_urgent', 0) > 0 else "No",
            pain="Yes" if row.get('has_pain_points', 0) > 0 else "No",
            skills=", ".join(row.get('skills', [])) if isinstance(row.get('skills', []), list) else "N/A"
        )

        # Try LLM summarization if enabled
        if use_llm and summarizer:
            try:
                response = summarizer(filled, max_length=100, min_length=30, do_sample=False)
                summary = response[0]['summary_text']
            except Exception as e:
                print(f"⚠️ LLM summarization failed: {e}")
                summary = filled  # fallback
        else:
            summary = filled

        summaries.append(summary)

    print("✅ Generated summaries.")
    return summaries
