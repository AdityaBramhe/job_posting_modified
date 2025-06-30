URGENT_PHRASES = ["asap", "immediate join", "urgent", "start immediately"]

def detect_urgency(description):
    desc = description.lower()
    return any(phrase in desc for phrase in URGENT_PHRASES)
