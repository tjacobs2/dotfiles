#!/usr/bin/python


from OneUSMInterfaceBasic import oneUSM_interface_residues
from pymol import cmd
from pymol import util


def zn_interface():

    cmd.show( 'cartoon' )
    cmd.hide( 'lines', 'elem H' )
    util.cbc("elem C")
    cmd.show( 'sticks', 'resn znx')

    cmd.set('cartoon_transparency','0.5')
    cmd.hide( 'sticks', 'elem H' )

    loaded_objs = cmd.get_names('objects')
    print loaded_objs

    for obj in loaded_objs :
        cmd.dist( '"'+obj+'_polar_conts"','"'+obj+'"','"'+obj+'"',quiet=1,mode=2,label=0,reset=1)
        cmd.enable("'"+obj+'_polar_conts"')


cmd.extend("zn_interface", zn_interface )
