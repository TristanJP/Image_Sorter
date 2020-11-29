"""
Docstring
"""

import sys
from image_sorter.file_handler import FileHandler

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # Main Routine Here

    fh = FileHandler(["T"])
    fh.greet()

    print("Yo Angelo")


    # Arg Parsing Here

if __name__ == "__main__":
    sys.exit(main())