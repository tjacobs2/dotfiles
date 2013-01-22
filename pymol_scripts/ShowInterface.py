#!/usr/bin/python

#script to read in a matcher generated pdb file, figure out the catalytic sidechains, and carry out some basic python commands

from pymol import cmd
from pymol import util

#takes in an interface definition file and displays it for ALL pdbs 
def showinterface( intdef_file ):

    cmd.show( 'cartoon' )
    #get rid of old stuffs
    cmd.hide( 'lines' )
    cmd.hide( 'sticks' )
    
    lines = open( intdef_file ).readlines()
    for line in lines :
	selset = 'res ' + line.split(" " )[1][:-1] + ' and chain ' + line.split(" " )[ 0 ]
	#print selset
        cmd.show( 'sticks', selset )

    cmd.set('cartoon_transparency','0.4')
    util.cbc("elem C") #colors by chain
    cmd.hide( 'sticks', 'elem H' )
    cmd.hide( 'lines', 'elem H' )

#color by chain cleanup
def chaincleanup():
    cmd.hide("(solvent and (all))")
    #cmd.hide("(all and hydro)")
    cmd.show("cartoon"   ,"all")
    util.color_chains("(all and elem c)",_self=cmd)
    cmd.show("sticks","((byres (all))&n;ca,c,n,o,h)")
    cmd.hide("(all and hydro)")
    #cmd.set('cartoon_transparency','0.25')
    cmd.hide( 'sticks', 'elem H' )
    cmd.hide( 'lines', 'elem H' )

#clean up but leave default colors
def cleanup():
    cmd.hide("(solvent and (all))")
    cmd.show("sticks","((byres (all))&n;ca,c,n,o,h)")
    cmd.show("lines","((byres (all))&(!(n;c,o,h|(n. n&!r. pro))))")
    cmd.hide("(all and hydro)")
    #cmd.set('cartoon_transparency','0.25')
    cmd.show("cartoon"   ,"all")

def showwater():
    cmd.show("(solvent and (all))")


def sel_from_reschain_set( resch_set ) :
    resch_sel = ""
    for resch in resch_set :
        resch_sel += "( res " + resch.split(" ")[1] + " and chain " + resch.split(" ")[0] + ") or "
    resch_sel = resch_sel[:-4] # get rid of the last "or"
    return resch_sel

def contrastinterface( pdb4char ) :
    cmd.show( 'cartoon' )
    cmd.hide( 'lines' )
    util.cbc( 'elem C' )
    cmd.set('cartoon_transparency','0.5')
    
    v3_lines = open( "/home/andrew/rosetta/interface_seqrec_benchmark/pdbs/v3/interface_definitions/" + pdb4char + "_dsintdef.txt" ).readlines()
#    benlines = open( "/home/andrew/rosetta/interface_seqrec_benchmark/pdbs/ben8Acut/interface_definitions/" + pdb4char + "_dsintdef.txt" ).readlines()
#    benlines = open( "/home/andrew/rosetta/interface_seqrec_benchmark/pdbs/benV3dup_A/interface_definitions/" + pdb4char + "_dsintdef.txt" ).readlines()
#    benlines = open( "/home/andrew/rosetta/interface_seqrec_benchmark/pdbs/benV3dup_B/interface_definitions/" + pdb4char + "_dsintdef.txt" ).readlines()
    benlines = open( "/home/andrew/rosetta/interface_seqrec_benchmark/pdbs/benV3dup_C/interface_definitions/" + pdb4char + "_dsintdef.txt" ).readlines()

    v3 = set({})
    ben = set({})
    for line in v3_lines :
        v3.add( line.strip() )
    for line in benlines:
        ben.add( line.strip() )

    v3_not_ben = v3 - ben
    ben_not_v3 = ben - v3

    print "v3 size:", len( v3)
    print "ben size: ", len( ben)
    print "v3 not ben: ", len( v3_not_ben )
    print "ben not v3: ", len( ben_not_v3 )


    v3mben_sel = sel_from_reschain_set( v3_not_ben )
    benmv3_sel = sel_from_reschain_set( ben_not_v3 )
    common_sel = sel_from_reschain_set( v3.intersection( ben ) )

    print "v3mben_sel: ", v3mben_sel
    print "benmv3_sel: ", benmv3_sel

    if len(v3_not_ben):
        cmd.select( "v3", v3mben_sel )
        cmd.create( "v3obj", "v3" )
        cmd.show( "sticks", "v3obj" )
        cmd.color( "red", "v3obj" )
    if len(ben_not_v3):
        cmd.select( "ben", benmv3_sel )
        cmd.create( "benobj", "ben" )
        cmd.show( "sticks", "benobj" )
        cmd.color( "pink", "benobj" )
    if len(common_sel):
        cmd.select( "common", common_sel )
        cmd.create( "commonobj", "common" )
        cmd.show( "sticks", "commonobj" )

    cmd.hide( "sticks", "elem H" )
#    cmd.hide( "sticks", "name c+n+o" )


#cmd.extend("showdes",showdes)
cmd.extend("showinterface", showinterface )
cmd.extend("chaincleanup", chaincleanup )
cmd.extend("showwater", showwater)
cmd.extend("cleanup", cleanup)
#cmd.extend("contrastinterface", contrastinterface )
