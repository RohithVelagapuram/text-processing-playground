def clean_text(text):
    """
    Performs basic text cleaning:
    - Converts text to lowercase
    - Removes extra spaces
    """

    cleaned = text.lower()
    cleaned = " ".join(cleaned.split())
    return cleaned


if __name__ == "__main__":
    sample_text = "  This   is   a SAMPLE   text for   Processing.  "
    result = clean_text(sample_text)
    print("Original:", sample_text)
    print("Cleaned:", result)
