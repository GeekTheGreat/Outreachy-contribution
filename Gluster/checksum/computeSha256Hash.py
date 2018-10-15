#!/usr/bin/python3.5
# This program computes sha256 checksum of all files in the specified directory including subdirectories.
import hashlib
from gluster import gfapi

def computeHash(filename):
    """This function computes sha256 checksum of the file.
    Argument: filename (String) - path to the filename
    Return: hash - computed sha256 checksum of the file
    """
    hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byteBlock in iter(lambda: f.read(4096), b""):
            hash.update(byteBlock)
    return hash

# create and mount volume
myVol = gfapi.Volume("localhost", "replicatedVol")
myVol.mount()
# walk through directory
for (root, dirs, files) in myVol.walk("testdir", topdown = False, onerror = None, followlinks = False):
    for file in files:
        # create filepath
        filePath = root + "/" + file
        # compute sha256 checksum
        hash = computeHash(filePath)
        # print filepath and checksum
        print(filePath, "\t", hash.hexdigest())
# unmount volume
myVol.umount()
