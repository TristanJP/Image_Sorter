"""
Docstring
"""

import sys
import os
from image_sorter.sorter import Sorter


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # Main Routine Here

    #print(os.listdir("/mnt/f/Pictures/RichardJoSona"))

    # PHONE TEST INPUTS
    phone_test_dir = ["/mnt/f/Pictures/Phone/06_06_18", "/mnt/f/Pictures/Phone/08_11_17"]
    phone_test_save = ["/mnt/f/Pictures/Phone/image_hashes.json", "/mnt/f/Pictures/Phone/duplicates.json"]

    # JOSONA TEST INPUTS
    josona_test_dir = ["/mnt/f/Pictures/RichardJoSona"]
    josona_test_save = ["/mnt/f/Pictures/RichardJoSona/image_hashes.json", "/mnt/f/Pictures/RichardJoSona/duplicates.json"]

    # TEST WITH MANY DUPLICATES
    bad_test_dir = ["/mnt/f/Pictures/Phone/06_06_18", "/mnt/f/Pictures/Phone/08_11_17", "/mnt/f/Pictures/Phone/08_11_17"]
    bad_test_save = ["/mnt/f/Pictures/Phone/bad_image_hashes.json", "/mnt/f/Pictures/Phone/bad_duplicates.json"]

    inputs = {
        "phone": [
            phone_test_dir,
            phone_test_save
        ],
        "jo": [
            josona_test_dir,
            josona_test_save
        ],
        "bad": [
            bad_test_dir,
            bad_test_save
        ]
    }

    image_sorter = Sorter()
    image_sorter.hash_directories(inputs[args[0]][0])

    image_sorter.save_hash_dict(inputs[args[0]][1][0])

    image_sorter.list_duplicates()

    image_sorter.save_duplicates_dict(inputs[args[0]][1][1])


    # Arg Parsing Here

if __name__ == "__main__":
    sys.exit(main())
