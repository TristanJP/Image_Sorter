"""
Module Docstring
"""

import os
import json
import hashlib
from time import time
from imutils import paths

"""
Class for reading and hashing images in directories
"""
class Sorter:

    """
    Initialise Sorter
    """
    def __init__(self):
        self.image_hashes = {}
        self.image_count = 0

        self.duplicates = {}
        self.duplicate_count = 0

    """
    May be useful, but seems too slow for now
    """
    def read_file_bytes_buffered(self, image_path):
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

    """
    Fast image file reading
    """
    def read_file_bytes(self, image_path):
        # Fast
        with open(image_path, "rb") as image:
            image_bytes = image.read()
            return image_bytes

    """
    Hash image using SHA256
    """
    def hash_image_sha256(self, image_path):
        image_bytes = self.read_file_bytes(image_path)
        return hashlib.sha256(image_bytes).hexdigest()

    """
    Hash image using Blake2
    """
    def hash_image_blake2(self, image_path):
        image_bytes = self.read_file_bytes(image_path)
        return hashlib.blake2b(image_bytes).hexdigest()

    """
    Hash all images in a directory
    """
    def hash_all_images(self, directory_path):
        print(f"- Hashing \"{directory_path}\" ...")
        #bmh_hasher = cv2.img_hash.BlockMeanHash_create()

        # Get list of all images in directory using imutils
        image_paths = list(paths.list_images(directory_path))

        # Get number of files
        self.image_count += len(image_paths)

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

    """
    Hash all images in a list of directories
    """
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

    """
    Creates a list of all duplicate images
    """
    def list_duplicates(self):
        print("[INFO] Searching for duplicates:")
        for image_hash, image_list in self.image_hashes.items():
            if len(image_list) > 1:
                self.duplicate_count += len(image_list)
                self.duplicates[image_hash] = image_list
        print(f"- Total Duplicates: {self.duplicate_count} for {len(self.duplicates)} unique file(s).")

    """
    Save the Hashed Image dictionary as a JSON file
    """
    def save_hash_dict(self, save_path):
        print("[INFO] Saving Image Hash Dictionary:")
        self.save_json_file(self.image_hashes, save_path)

    """
    Save the Duplicates dictionary as a JSON file
    """
    def save_duplicates_dict(self, save_path):
        print("[INFO] Saving Duplicates Dictionary:")
        self.save_json_file(self.duplicates, save_path)

    """
    Save file
    """
    def save_json_file(self, content, save_path):
        print(f"- Saving to file location: \"{save_path}\"")
        with open(save_path, "w") as save_file:
            # Writes JSON file
            save_file.write(json.dumps(content))
        print("    done")