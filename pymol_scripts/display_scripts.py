#!/usr/bin/python

#Useful functions for prettying up structures

from pymol import cmd
from pymol import util

#color by chain cleanup
def cartoon():
	cmd.show("cartoon")
	cmd.hide("(solvent and (all))")
	cmd.hide("(all and hydro)")
	cmd.hide( 'sticks' )
	cmd.hide( 'lines' )
	color_chains(rainbow = 0)

def chain_cleanup():
	cleanup()
	color_chains(rainbow = 0)
	#util.color_chains("(all and elem c)",_self=cmd)

#clean up but leave default colors
def cleanup():
	#hide waters and hydrgoens
	cmd.hide("(solvent and (all))")
	cmd.hide("(all and hydro)")
	#show transparent cartoon
	cmd.show("cartoon"   ,"all")
	cmd.set('cartoon_transparency','0.25')
	#show mainchain sticks
	cmd.show("sticks","((byres (all))&n;ca,c,n,o,h)")
	#hide hydrogens
	cmd.hide( 'sticks', 'elem H' )
	cmd.hide( 'lines', 'elem H' )

def sewalign(first,second):
	#hide waters
	cmd.hide("(solvent and (all))")
	#hide hydrogens
	cmd.hide( 'sticks', 'elem H' )
	cmd.hide( 'lines', 'elem H' )

	#show cartoon
	cmd.show("cartoon"   ,"all")

	#create duplicate of first
	first_copy = first + "_copy"
	cmd.copy(first_copy, first)

	#select first 14 residues 
	cmd.select('node_9_selection', '(obj *_9_* and resi 1-14)')
	cmd.select('node_12_selection', '(obj *_12_* and resi 1-14)')
	cmd.select('node_15_selection', '(obj *_15_* and resi 1-14)')

	alignment_1 = cmd.align(first, 'node_9_selection')
	print alignment_1[0]

	alignment_2 = cmd.align(second, 'node_12_selection')
	print alignment_2[0]

	alignment_3 = cmd.align(first_copy, 'node_15_selection')
	print alignment_3[0]

def mainchain():
	#hide waters
	cmd.hide("(solvent and (all))")
	#hide cartoon
	cmd.hide("cartoon")
	cmd.hide("lines","not(name ca,c,n,o,h)")
	#show mainchain sticks
	cmd.show("sticks","((byres (all))&n;ca,c,n,o,h)")
	util.color_chains("(all and elem c)",_self=cmd)

cmd.extend("chain_cleanup", chain_cleanup )
cmd.extend("cleanup", cleanup)
cmd.extend("mainchain", mainchain )
cmd.extend("sewalign", sewalign )
cmd.extend("cartoon", cartoon )
