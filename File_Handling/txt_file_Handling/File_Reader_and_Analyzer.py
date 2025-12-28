total_line = 0
non_empty_lines = 0
total_words = 0
total_characters = 0
try:
    with open("sample.txt", "r") as file:
        for line in file:
            total_line += 1
            clean_line = line.strip()
            if clean_line != "":
                non_empty_lines += 1
                total_words += len(clean_line.split())
                total_characters += len(clean_line)
        print(f"""
Total Lines: {total_line}
Non-Empty Lines: {non_empty_lines}
Total Words: {total_words}
Total Characters: {total_characters}
""")


except FileNotFoundError:
    print("File Not Found")