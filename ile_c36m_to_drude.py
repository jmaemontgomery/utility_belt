#!/usr/bin/python
# Script to convert C36m ILE to drude nomenclature in CRDs and PDBs
# To do: add functionality to keep old version of file
import os
import argparse

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('-file', type=str, default=None, required=True,
                help='Input coordinate file (.pdb or .crd)')

cmd = ap.parse_args()
filepaths = [cmd.file]

for fp in filepaths:
    ext = os.path.splitext(fp)[-1].lower()

    if ext == ".crd":
        print (fp, "is an crd!")

        # Read in the file
        with open(fp, 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(' ILE       CD ', ' ILE       CD1')
        filedata = filedata.replace(' ILE       HD1 ', ' ILE       HD11')
        filedata = filedata.replace(' ILE       HD2 ', ' ILE       HD12')
        filedata = filedata.replace(' ILE       HD3 ', ' ILE       HD13')
        # Write the file out again
        with open(fp, 'w') as file:
            file.write(filedata)

    elif ext == ".pdb":
        print (fp, "is a pdb!")

        # Read in the file
        with open(fp, 'r') as file :
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(' CD  ILE', ' CD1 ILE')
        filedata = filedata.replace(' HD1 ILE', 'HD11 ILE')
        filedata = filedata.replace(' HD2 ILE', 'HD12 ILE')
        filedata = filedata.replace(' HD3 ILE', 'HD13 ILE')
        # Write the file out again
        with open(fp, 'w') as file:
            file.write(filedata)

    else:
        print (fp, "is an unknown file format.")

