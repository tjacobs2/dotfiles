#!/usr/bin/python

from pymol import cmd
from pymol import util
from pdb_structure import PDBStructure, Atom, Residue, Chain
from find_neighbors import find_interface_pointing_residue

def init_pdb_structures():
    loaded_objs = cmd.get_names('objects')
    pdb_structures = []
    for obj in loaded_objs :
        print obj
        atoms = cmd.get_model(obj)
        pdb = PDBStructure()
        chain = Chain()
        residue = Residue()
        for at in atoms.atom :
            #print at.chain, at.resn, at.resi, at.name, at.index, at.b,at.coord[0],at.coord[1],at.coord[2]
            if chain.chain_name != "" and chain.chain_name != at.chain :
                #print "appending chain", chain.chain_name, "to object", obj
                chain.add_residue( residue )
                residue = Residue()
                pdb.add_chain( chain )
                chain = Chain()
            elif residue.resstring != "" and residue.resstring != str( at.resi ) :
                #print "appending residue", residue.resstring, "to chain", chain.chain_name
                chain.add_residue( residue )
                residue = Residue()
            newat = Atom()
            newat.xyz.x_ = at.coord[0]
            newat.xyz.y_ = at.coord[1]
            newat.xyz.z_ = at.coord[2]
            newat.name = at.name
            newat.pdb_index = at.index
            if residue.resstring == "" :
                residue.resstring = str(at.resi )
                residue.resname = at.resn
                if chain.chain_name == ""  :
                    chain.chain_name = at.chain
            assert( chain.chain_name != "" )
            residue.add_atom( newat )
        pdb_structures.append( pdb )

    return pdb_structures

def find_interface_residues_from_pymol_objects() :
    loaded_objs = cmd.get_names('objects')
    pdb_structures = init_pdb_structures()
    #print "read in", len(pdb_structures), "pdb structures"
    for i in xrange(len(pdb_structures)):
        obj = loaded_objs[i]
        pdb = pdb_structures[i]
        intres = find_interface_pointing_residue( pdb )
        #print "interface res dictionary size", len(intres.keys() )
        select_string = ""
        for c in intres.keys() :
            #print "chain", c, "size", len(intres[c])
            for r in intres[c] :
                select_string += "("+obj+" and chain " + c + " and res " + r + " ) or "
        select_string = select_string[:-4]
        #print select_string
        selecting.select( obj + "intres", select_string )


cmd.extend("init_pdb_structures", find_interface_residues_from_pymol_objects )
