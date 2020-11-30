"""
Docstring
"""

import cv2
from imutils import paths
import os
import argparse
import json

class Sorter:

    def __init__(self):
        self.image_hashes = {}

    def hash_image(self, image):
        # Convert to grayscale
        cvt_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Resize to 9x8
        cvt_image = cv2.resize(cvt_image, (9, 8))

        # Compute the relative horizontal gradient between adjacent coloumn pixels
        diff = cvt_image[:, 1:] > cvt_image[:, :-1]

        # Convert the difference image to a hash and return
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

    def hash_all_images(self, directory_path):
        print(f"- Hashing \"{directory_path}\" ...")
        #bmh_hasher = cv2.img_hash.BlockMeanHash_create()

        # Get list of all iamges in directory
        image_paths = list(paths.list_images(directory_path))

        # Iterate over image paths
        for image_path in image_paths:
            # Read and hash image
            image = cv2.imread(image_path)
            hashed_image = self.hash_image(image)
            #hashed_image = bmh_hasher.compute(image)

            # Check hash dictionary to see if it already contains the image hash
            # If hash doesn't exist already, return empty list
            image_hash = self.image_hashes.get(hashed_image, [])

            # Append image path to list
            image_hash.append(image_path)

            # Add image hash to hashed image dictionary with path list value
            self.image_hashes[hashed_image] = image_hash
        print("    done")

    def hash_directories(self, directory_paths):
        print("[INFO] Hashing all images in directory list:")
        for path in directory_paths:
            if os.path.isdir(path):
                self.hash_all_images(path)
            else:
                print(f"[WARNING] Invalid directory: \"{path}\"\n  continuing...")
        print("[INFO] All valid directories hashed.")

    def save_hash_dict(self, save_path):
        print(f"[INFO] Saving image hashes to \"{save_path}\"")
        with open(save_path, "w") as save_file:
            save_file.write(json.dumps(self.image_hashes))
        print("    done")