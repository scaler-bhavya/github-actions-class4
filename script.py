# def greet(name):
#     print(f"Hello, {name}!")


# greet("John")

# def add(a, b):
#     return a + b

import sys

def main():
    try:
        # Get the name from the command line arguments
        name = sys.argv[1] if len(sys.argv) > 1 else "GitHub User"
        greeting = f"Hello, {name}!"
        print(greeting)
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()
