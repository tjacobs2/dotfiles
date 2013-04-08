#!/usr/bin/python

#Useful functions for prettying up structures

from pymol import cmd
from pymol import util

#color by chain cleanup
def chain_cleanup():
	cleanup()
	util.color_chains("(all and elem c)",_self=cmd)

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
