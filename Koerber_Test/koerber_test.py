
import pyperclip
import re
import sys
import time

def check_invalid(str1):
    # Get clipboard content
    print("Hi")

    clipboard_content = pyperclip.paste()

    # Regular expression to find the location code
    match = re.search(f'{str1}', clipboard_content)

    if match:
        print(6)
        sys.exit(6)
    else:
        print(5)
        sys.exit(5)

# Call the function
check_invalid(sys.argv[1])
# check_invalid("RFOUTB")

