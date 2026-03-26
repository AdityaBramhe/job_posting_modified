# urgency_detector.py

URGENT_PHRASES = ["asap", "immediate", "urgent", "join immediately"]

def detect_urgency(description):
    desc = description.lower()
    return any(word in desc for word in URGENT_PHRASES)