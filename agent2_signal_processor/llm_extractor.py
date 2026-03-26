# llm_extractor.py

import subprocess
import json
import re

def extract_signals_with_llama3(description: str):
    try:
        prompt = f"Extract skills and urgency from this job:\n{description[:1000]}"

        result = subprocess.run(
            ["ollama", "run", "llama3"],
            input=prompt.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=20
        )

        output = result.stdout.decode()

        match = re.search(r'\{.*\}', output, re.DOTALL)
        if match:
            return json.loads(match.group())

    except Exception as e:
        print("⚠️ LLM failed, skipping...", e)

    return {}