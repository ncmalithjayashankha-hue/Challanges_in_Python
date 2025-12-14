## Advanced Log Analyzer: Corrected

# 1. Initialize the dictionaries
complete_message = {"INFO": 0, "WARNING": 0, "ERROR": 0}
suspicious = {"failed": 0, "timeout": 0, "unauthorized": 0}

# 2. Get the filename from the user
file_name = input("Enter file name: ")
lines_analyzed = 0

# 3. Use try/except with the recommended 'with open' structure
try:
    with open(file_name, "r") as file_log:
        for line in file_log:
            lines_analyzed += 1

            # Split the line only once. Use strip() to remove newlines/whitespace.
            line_parts = line.strip().split()

            # CRITICAL FIX: Ensure the list is long enough before accessing elements
            if not line_parts:
                # Skip empty lines
                continue

            # --- Log Type Analysis (First Word) ---
            log_type = line_parts[0].upper().replace(":", "")

            if log_type in complete_message:
                complete_message[log_type] += 1
            else:
                print(f"Skipping line {lines_analyzed}: Unknown primary log type '{log_type}'")

            # --- Suspicious Event Analysis (Second Word) ---

            # FIX 2: Check for the second word's existence before accessing line_parts[1]
            if len(line_parts) > 1:
                susp_type = line_parts[1].lower().replace(":", "")

                if susp_type in suspicious:
                    suspicious[susp_type] += 1
                # Removed the redundant 'else' print for unknown suspicious type

            # LOGICAL ERROR FIX: Ensure only the log level is printed for primary log type skip.
            # The original code printed "Skipping line..." again here, which was likely a copy-paste error.

# Handle the case where the file doesn't exist
except FileNotFoundError:
    print(f"ERROR: File '{file_name}' Not Found")
    # Exit the program since we can't analyze anything
    exit()

# 4. Print Summary (After the file is automatically closed)
print("\n--- Analysis Complete ---")

# FIX 3: Get the key with the maximum value for "Most Suspicious Log Level"
# The original code only returned the key name, not the value.
most_suspicious_key = max(suspicious, key=suspicious.get)

print(f"""
==== LOG Summary ====
Total Lines Analyzed    : {lines_analyzed}
INFO                    : {complete_message["INFO"]}
WARNING                 : {complete_message["WARNING"]}
ERROR                   : {complete_message["ERROR"]}

==== Security Alerts ====
failed                      : {suspicious["failed"]}
timeout                     : {suspicious["timeout"]}
unauthorized                : {suspicious["unauthorized"]}

Most Suspicious Event       : {most_suspicious_key} ({suspicious[most_suspicious_key]} counts)
""")