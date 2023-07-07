#!/usr/bin/python
# Functions to use to complete a window of umbrella sampling 
import re
import MDAnalysis as mda
import argparse

ap = argparse.ArgumentParser(description=__doc__)
ap.add_argument('-umbrella', action='store_true',
                help='Flag to enable umbrella sampling.')
ap.add_argument('-r0', type=float, default=0, 
                help="R0")
ap.add_argument('-k', type=float, default=4184.0, 
                help="Force restraint. Default is 10 kcal mol-1 angstrom-1 or 4184 kj mol-1 nm-1")

def segment_select(universe: mda.core.universe, segid: str, not_heavy: str):
	segid = segid.upper()
	selected = universe.select_atoms(f"segid {segid} and not ({not_heavy})")

	group = []

	for i in selected:
		selected_index = re.findall('Atom (\d+)', str(i))
		group.append(int(selected_index[0]) - 1)

	return group

# Select lipid atoms, not drudes or LP or hydrogen 
def drude_lipid_sele(universe: mda.core.universe):
    return segment_select(universe, "MEMB", "name D* or name LP* or name H*")

# Select segid atoms, not drudes, LP or hydrogen
def drude_segid_sele(universe: mda.core.universe):
    return segment_select(universe, "IBUT", "name D* or name LP* or name H*")
