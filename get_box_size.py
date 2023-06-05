#!/usr/bin/python
# Pull box size from OpenMM-style state file (in nm) & replace it in target file (in angstrom)
# Assumes target to be styled "<BOXX>", "<BOXY>", and "<BOXZ>"

# To do: Edit to include user flags for file names and string to replace with box size

rstfile = "/path/to/rstfile.rst"
targetfile = "/path/to/target/to/change.inp"

f = open(rstfile, 'r')

box = {}

# Read in box size from rst file
while True:
    line = f.readline()
    if not line: break

    if line.split()[0] == "<A":
        size = line.split()[1].strip('x="')
        box['A'] = str(float(size)*10)
    elif line.split()[0] == "<B":
        size = line.split()[2].strip('y="')
        box['B'] = str(float(size)*10)
    elif line.split()[0] == "<C":
        size = line.split()[3].strip('z="').strip('"/>')
        box['C'] = str(float(size)*10)
    else:
        pass

# Print to show box size was correctly stripped
print(box)

# Read in the target file
with open(targetfile, 'r') as file :
    filedata = file.read()

# Replace the target string, in this case box vectors
filedata = filedata.replace('<BOXX>', box.get('A'))
filedata = filedata.replace('<BOXY>', box.get('B'))
filedata = filedata.replace('<BOXZ>', box.get('C'))

# Write the new edited file
with open(targetfile, 'w') as file:
    file.write(filedata)
