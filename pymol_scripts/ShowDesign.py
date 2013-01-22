#!/usr/bin/python

#script to read in a matcher generated pdb file, figure out the catalytic sidechains, and carry out some basic python commands

from pymol import cmd
from pymol import util


def showdes(desname=None):
    
    loaded_objs = cmd.get_names('objects')
    print loaded_objs

    if desname == None and not(loaded_objs): 
        print 'Error: please load a file'
        return 1
    elif desname == None:
        desname = loaded_objs[0]+'.pdb'

    read_file = open(desname,'r')

    cat_res = []

    for line in read_file:
        if line[0:4] == 'ATOM': break
        if line[0:24] == 'REMARK BACKBONE TEMPLATE':
            cols = line.split()
            cat_res.append(cols[10])
        elif line[0:24] == 'REMARK   0 BONE TEMPLATE':
            cols = line.split()
            cat_res.append(cols[11])

    read_file.close()
    #print cat_res
    
    cat_string = 'resi '
    for resis in cat_res:
        cat_string = cat_string + resis + '+'
    
    cat_string = cat_string[:-1] #take away last +
   
    print cat_string
   
    cmd.select('lig','het and !name V*')
    cmd.select('cats',cat_string)
    cmd.select('acts','lig around 10 and !cats and !name V* and !lig')
    cmd.hide('lines')
    cmd.show('sticks','lig')
    cmd.show('sticks','cats')
    cmd.show('car')
    cmd.select('acts','(byres acts) and !hydro',enable=0)
    cmd.set('cartoon_transparency','0.5')
    util.cba(11,'cats')

cmd.extend("showdes",showdes)
