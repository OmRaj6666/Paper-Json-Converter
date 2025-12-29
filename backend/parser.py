import re

def parse_text(text):
    """
    Parse extracted text into structured JSON
    """
    data = {}

    patterns = {
        "name": r"Name\s*:\s*(.*)",
        "roll_no": r"Roll\s*No\s*:\s*(.*)",
        "department": r"Department\s*:\s*(.*)",
        "college": r"College\s*:\s*(.*)"
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, text, re.IGNORECASE)
        data[key] = match.group(1).strip() if match else None

    return data
