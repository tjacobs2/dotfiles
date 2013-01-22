#!/usr/bin/python

from pymol import cmd
from pymol import util
from create_interface_selection import create_interface_selections

def find_and_show_interface() :
    cmd.show( 'cartoon' )
    cmd.hide( 'lines', 'elem H' )

    cmd.set('cartoon_transparency','0.5')
    util.cbc("elem C")

    loaded_objs = cmd.get_names('objects')
    create_interface_selections()
    for obj in loaded_objs :
        cmd.show( "sticks", obj+"intres" )

    cmd.hide( 'sticks', 'elem H' )
        

cmd.extend("find_and_show_interface", find_and_show_interface )
