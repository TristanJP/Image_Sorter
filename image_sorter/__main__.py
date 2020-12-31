"""
Docstring
"""

import sys
import os
import argparse
from image_sorter.sorter import Sorter


def main(args):

    # Main Routine Here

    #print(os.listdir("/mnt/f/Pictures/RichardJoSona"))

    # VIDEO TEST INPUTS
    video_test_dir = ["/mnt/c/Users/TP185123/Videos/GMA500", "/mnt/c/Users/TP185123/Videos"]
    video_test_save = ["/mnt/c/Users/TP185123/Videos/image_hashes.json", "/mnt/c/Users/TP185123/Videos/duplicates.json"]

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
        ],
        "videos": [
            video_test_dir,
            video_test_save
        ]
    }


    image_sorter = Sorter(args.origin_paths)
    image_sorter.hash_directories(inputs[args[0]][0], cmd)

    image_sorter.save_hash_dict(inputs[args[0]][1][0])

    image_sorter.save_duplicates_dict(inputs[args[0]][1][1])


    Arg Parsing Here


# Create arg parser
parser = argparse.ArgumentParser(
    description="Iterates over directories of media files and identifies duplicates using a hashing algorithm."
)

# Add cmd arg
parser.add_argument(
    "cmd",
    choices=["list", "copy", "move", "delete"],
    help="""
    The command options:
    list - List all duplicates,
    copy - Copy all unique files to target location,
    move - Move all unique files to target location,
    delete - Delete all duplicate files (Cannot be undone!).
    """
)

# Add all origin paths arg
parser.add_argument(
    "origin-paths",
    nargs="+",
    help="The origin paths that point to the directories containing the images to be sorted."
)

# Add target path arg (required for copy and move)
parser.add_argument(
    "--target-path",
    nargs=1,
    help="The target path where the unique files will be copied/moved to."
)

# Parse the args
args = parser.parse_args()

# Check that target path present for copy and move cmd
if args.cmd in ["copy", "move"] and not hasattr(args, "target-path"):
    parser.error(f"{args.cmd} requires --target-path.")

sys.exit(main(args))
