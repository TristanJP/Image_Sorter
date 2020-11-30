"""
Docstring
"""

import sys
from image_sorter.sorter import Sorter

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # Main Routine Here

    image_sorter = Sorter()
    image_sorter.hash_directories(["/mnt/f/Pictures/RichardJoSona"])

    image_sorter.save_hash_dict("/mnt/f/Pictures/RichardJoSona/image_hashes.json")


    # Arg Parsing Here

if __name__ == "__main__":
    sys.exit(main())