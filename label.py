def normalize_label(label):
    if not isinstance(label, str):
        return None

    label = label.strip().lower()

    if label in ("+", "cross"):
        return "Cross"

    if label == "x":
        return "X"

    return None
