#!/usr/bin/python
# Pull box size from OpenMM-style state file (in nm) & replace it in target file (in angstrom)
# Assumes target to be styled "<BOXX>", "<BOXY>", and "<BOXZ>"
import argparse

parser = argparse.ArgumentParser(description='Scrape a box size from an OpenMM-Style state file (in nm) & replace it in a target file (in angstrom). Assumes your target file is styled "<BOXX>", "<BOXY>", and "<BOXZ>" where you want it replaced, unless user defines differently')

parser.add_argument('-rstFile', type = str, required = True, help = 'Path to your RST file.')
parser.add_argument('-targetFile', type = str, required = True, help = 'Path to your target file.')
parser.add_argument('-replaceX', type = str, default = "<BOXX>", help = 'Change target phrase (default "<BOXX>")')
parser.add_argument('-replaceY', type = str, default = "<BOXY>", help = 'Change target phrase (default "<BOXY>")')
parser.add_argument('-replaceZ', type = str, default = "<BOXZ>", help = 'Change target phrase (default "<BOXZ>")')

args = parser.parse_args()

rstfile = args.rstFile
targetfile = args.targetFile

f = open(rstfile, 'r')

box = {}

# Read in box size from rst file
while True:
    line = f.readline()
    if not line: break

    if line.split()[0] == "<A":
        size = line.split()[1].strip('x="')
        box['X'] = str(float(size)*10)
    elif line.split()[0] == "<B":
        size = line.split()[2].strip('y="')
        box['Y'] = str(float(size)*10)
    elif line.split()[0] == "<C":
        size = line.split()[3].strip('z="').strip('"/>')
        box['Z'] = str(float(size)*10)
    else:
        pass

# Print to show box size was correctly stripped
print(box)

# Read in the target file
with open(targetfile, 'r') as file :
    filedata = file.read()

# Replace the target string, in this case box vectors
filedata = filedata.replace(args.replaceX, box.get('X'))
filedata = filedata.replace(args.replaceY, box.get('Y'))
filedata = filedata.replace(args.replaceZ, box.get('Z'))

# Write the new edited file
with open(targetfile, 'w') as file:
    file.write(filedata)
