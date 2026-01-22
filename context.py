def classify_context(text: str) -> str:
    t = text.lower()
    if any(k in t for k in ["integral", "derivative", "="]):
        return "math"
    if any(k in t for k in ["which", "best answer"]):
        return "mcq"
    return "conceptual"
