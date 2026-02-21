import sys


def filter_lines(file_path, keyword):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    matches = [line.strip() for line in lines if keyword.lower() in line.lower()]

    print(f"\nLines containing '{keyword}':\n")

    if matches:
        for line in matches:
            print("-", line)
    else:
        print("No matches found.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python keyword_filter.py <file_path> <keyword>")
    else:
        filter_lines(sys.argv[1], sys.argv[2])
