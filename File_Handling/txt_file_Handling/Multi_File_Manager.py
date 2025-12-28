import os

folder_path = "Text_Files"
if not os.path.exists(folder_path):
    print("Folder doesn't exist")
    exit()

all_files = os.listdir(folder_path)
txt_files = [f for f in all_files if f.endswith(".txt")]
print(txt_files)
with open("Summary_Report.txt", "w") as g:
    g.write("==== Multi File Analysis ====\n\n")

for txt_file in txt_files:
    total_line = 0
    non_empty_lines = 0
    total_words = 0
    total_characters = 0

    with open(os.path.join(folder_path, txt_file), "r") as f:
        for line in f:
            total_line += 1
            clean_line = line.strip()
            if clean_line != "":
                non_empty_lines += 1
                total_words += len(clean_line.split())
                total_characters += len(clean_line)
        with open("Summary_Report.txt", "a") as h:
                h.write(f"""
---- {txt_file} ----
Total Lines: {total_line}
Non-Empty Lines: {non_empty_lines}
Total Words: {total_words}
Total Characters: {total_characters}
""")
        print(f"""
Total Lines: {total_line}
Non-Empty Lines: {non_empty_lines}
Total Words: {total_words}
Total Characters: {total_characters}
""")



with open("backup.log", "a") as file:
    file.write(f"Multi - file analysis completed\n")