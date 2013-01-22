#!/usr/bin/python

from pymol import cmd
from pymol import util
from pdb_structure import PDBStructure, Atom, Residue, Chain
#from find_neighbors import find_interface_pointing_residue

def init_pdb_structs():
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
        chain.add_residue(residue)
        pdb.add_chain(chain)
        pdb_structures.append( pdb )

    return pdb_structures

