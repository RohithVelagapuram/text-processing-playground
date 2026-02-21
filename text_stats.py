import sys
from collections import Counter


def analyze_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()

    words = text.lower().split()
    word_count = len(words)

    sentences = text.count('.') + text.count('!') + text.count('?')
    common_words = Counter(words).most_common(5)

    print("Total Words:", word_count)
    print("Total Sentences:", sentences)
    print("Top 5 Words:")
    for word, freq in common_words:
        print(f"{word}: {freq}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python text_stats.py <file_path>")
    else:
        analyze_text(sys.argv[1])
