from datetime import datetime

log_file = "test_output.txt"

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(log_file, "a") as file:
    file.write(f"Test script executed at: {now}\n")