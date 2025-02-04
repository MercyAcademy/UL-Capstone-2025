from datetime import datetime

# Print a message with the current timestamp
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"Test script executed at: {now}")

# Write the output to a file (optional, for debugging)
with open("test_output.txt", "a") as file:
    file.write(f"Test script executed at: {now}\n")