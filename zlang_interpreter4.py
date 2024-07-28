import sys
import re

def main():
    code = sys.argv[1]

    # Example Z-Lang syntax:
    # "spill 'Hello, world!'"  (prints "Hello, world!")
    # "ask 'What is your name?'"  (prompts the user for input)

    match = re.match(r"spill\s+'(.*)'\s*", code)
    if match:
        output = match.group(1)
        print(output)  # Print the matched text
    else:
        match = re.match(r"ask\s+'(.*)'\s*", code)
        if match:
            question = match.group(1)
            # Read input from standard input (stdin)
            user_input = sys.stdin.readline().strip()
            print(user_input)  # Print the user's input
        else:
            print("Invalid Z-Lang code.")

if __name__ == '__main__':
    main()