"""
Docstring
"""

import cv2
from imutils import paths
import os
import argparse
import json
import hashlib
from time import time

class Sorter:

    def __init__(self):
        self.image_hashes = {}
        self.image_count = 0

    """
    Manual Image Hasher using OpenCV
    """
    def hash_image_difference(self, image):
        # Convert to grayscale
        cvt_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Resize to 9x8
        cvt_image = cv2.resize(cvt_image, (9, 8))

        # Compute the relative horizontal gradient between adjacent coloumn pixels
        diff = cvt_image[:, 1:] > cvt_image[:, :-1]

        # Convert the difference image to a hash and return
        return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

    def read_file_bytes_buffered(self, image_path):
        # Slow
        BUFFER_SIZE = 16384  # 16kB
        b = b""
        with open(image_path, "rb") as image:
            while True:
                # Read in 16kB from image file
                bytes_read = image.read(BUFFER_SIZE)
                if bytes_read:
                    b += bytes_read
                else:
                    # No more bytes
                    break
        return b

    def read_file_bytes(self, image_path):
        # Fast
        with open(image_path, "rb") as image:
            image_bytes = image.read()
            return image_bytes

    def hash_image_sha256(self, image_path):
        image_bytes = self.read_file_bytes(image_path)
        return hashlib.sha256(image_bytes).hexdigest()

    def hash_image_blake2(self, image_path):
        image_bytes = self.read_file_bytes(image_path)
        return hashlib.blake2b(image_bytes).hexdigest()

    def hash_all_images(self, directory_path):
        print(f"- Hashing \"{directory_path}\" ...")
        #bmh_hasher = cv2.img_hash.BlockMeanHash_create()

        # Get list of all iamges in directory
        image_paths = list(paths.list_images(directory_path))
        self.image_count += len(image_paths)
        tht = 0
        # Iterate over image paths
        for image_path in image_paths:
            # Hash image (Blake2 fastest)

            hashed_image = self.hash_image_blake2(image_path)

            # Check hash dictionary to see if it already contains the image hash
            # If hash doesn't exist already, return empty list
            image_hash = self.image_hashes.get(hashed_image, [])

            # Append image path to list
            image_hash.append(image_path)

            # Add image hash to hashed image dictionary with path list value
            self.image_hashes[hashed_image] = image_hash
        print("    done")


    def hash_directories(self, directory_paths):
        t = time()
        self.image_count = 0
        print("[INFO] Hashing all images in directory list:")
        for path in directory_paths:
            if os.path.isdir(path):
                self.hash_all_images(path)
            else:
                print(f"[WARNING] Invalid directory: \"{path}\"\n  continuing...")
        print("[INFO] All valid directories hashed.")
        elapsed = time() - t
        print(f"- Total Images Hashed: {self.image_count}\n- Time taken: {elapsed}")

    def save_hash_dict(self, save_path):
        print("[INFO] Saving Image Hash Dictionary:")
        print(f"- Saving to file location: \"{save_path}\"")
        with open(save_path, "w") as save_file:
            save_file.write(json.dumps(self.image_hashes))
        print("    done")