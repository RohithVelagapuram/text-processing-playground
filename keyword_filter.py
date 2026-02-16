# keyword_filter.py
# Filters and displays lines that contain a given keyword.

def filter_lines(file_path, keyword):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        matches = [line.strip() for line in lines if keyword.lower() in line.lower()]

        print(f"\nLines containing '{keyword}':\n")

        if matches:
            for line in matches:
                print("-", line)
        else:
            print("No matches found.")

    except FileNotFoundError:
        print("File not found. Please check the path.")

if __name__ == "__main__":
    path = input("Enter file path: ")
    keyword = input("Enter keyword to search: ")
    filter_lines(path, keyword)
