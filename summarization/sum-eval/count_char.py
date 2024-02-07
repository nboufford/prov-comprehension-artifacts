import sys

# Check if a filename is provided as a command-line argument
if len(sys.argv) != 2:
    print("Usage: python count_characters.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    # Open the file and read its content
    with open(filename, 'r') as file:
        content = file.read()
        char_count = len(content)
        print(char_count)

except FileNotFoundError:
    print(f"File not found: {filename}")
    sys.exit(1)