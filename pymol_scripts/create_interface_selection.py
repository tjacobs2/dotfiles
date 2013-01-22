#!/usr/bin/python

from pymol import cmd
from pymol import util
from pymol import selecting
from pdb_structure import PDBStructure, Atom, Residue, Chain
from find_neighbors import find_interface_pointing_residue
from initialize_pdb_structures_from_pymol_objects import init_pdb_structs

def create_interface_selections() :
    loaded_objs = cmd.get_names('objects')
    pdb_structures = init_pdb_structs()
    print "read in", len(pdb_structures), "pdb structures"
    for i in xrange(len(pdb_structures)):
        obj = loaded_objs[i]
        pdb = pdb_structures[i]
        for j in xrange(len(pdb.chains)) :
            print "Found chain", pdb.chains[j].chain_name
        print "Found", len( pdb.chains ), "chains"
        intres = find_interface_pointing_residue( pdb )
        print "interface res dictionary size", len(intres.keys() )
        select_string = ""
        for c in intres.keys() :
            print "chain", c, "size", len(intres[c])
            for r in intres[c] :
                select_string += "("+obj+" and chain " + c + " and res " + r + " ) or "
        select_string = select_string[:-4]
        #print select_string
        selecting.select( obj + "intres", select_string )


cmd.extend("create_interface_selections", create_interface_selections )
