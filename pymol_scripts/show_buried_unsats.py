from pymol.cgo import *
from pymol import cmd

def read_buried_unsats_from_logfile( fname ):
    buns = []
    for line in [x.strip() for x in open( fname ).readlines() ] :
        cols = line.split()

        if len(cols) == 0 : continue
        if cols[0] == "CalcOutput:" and cols[ 14 ] == "1":
            #m = cmd.get_model(cols[2])
            sel = cmd.index( "resi " + cols[6] + " and name " + cols[8], 1 )
            buns.append( (cols[2], sel[ 0 ][ 1 ] - 1) ) # index of the atom with a buried-unsatisfied hydrogen bonding group
    return buns

def append_sphere_objs_from_atoms( buns_atoms, obj ) :
    for buns_atom in buns_atoms :
        print buns_atom
        #for line in [ x.strip() for x in open( fname ).readlines() ] :
        #print line
        m = cmd.get_model( buns_atom[0] )
        at = m.atom[ buns_atom[1] ]
        #print sel, at
        #coords = cmd.get_coord( cols[6] + "/" + cols[8] )
        #print coords[0], coords[1], coords[2], cols[6], cols[8]
        obj.extend( [ SPHERE, at.coord[0], at.coord[1], at.coord[2], 0.7 ] )


# show all buried unsatisfied hydrogen bonding groups
def buried_unsats_from_logfile( fname ) :
    obj = []
    white =  [ COLOR, 1.0, 1.0, 1.0 ]
    #blue = [ COLOR, 0.0, 0.0, 1.0 ]
    #red  = [ COLOR, 1.0, 0.0, 0.0 ]

    #obj.extend( red )
    #obj.extend( blue )
    obj.extend( white )
    atoms = read_buried_unsats_from_logfile( fname )
    append_sphere_objs_from_atoms( atoms, obj )
    cmd.load_cgo(obj,'test',1)

def contrast_unsats_logfile( fname1, fname2 ) :
    white =  [ COLOR, 1.0, 1.0, 1.0 ]
    blue = [ COLOR, 0.0, 0.0, 1.0 ]
    red  = [ COLOR, 1.0, 0.0, 0.0 ]

    atoms1 = read_buried_unsats_from_logfile( fname1 )
    atoms2 = read_buried_unsats_from_logfile( fname2 )

    set_ats1 = set( atoms1 )
    set_ats2 = set( atoms2 )

    ats_intersect = set_ats1.intersection( set_ats2 )
    ats_1_absent_2 = set_ats1.difference( set_ats2 )
    ats_2_absent_1 = set_ats2.difference( set_ats1 )

    obj_common = []
    obj_common.extend( white )
    append_sphere_objs_from_atoms( ats_intersect, obj_common )

    obj_diff1 = []
    obj_diff1.extend( blue )
    append_sphere_objs_from_atoms( ats_1_absent_2, obj_diff1 )

    obj_diff2 = []
    obj_diff2.extend( red )
    append_sphere_objs_from_atoms( ats_2_absent_1, obj_diff2 )

    cmd.load_cgo(obj_common,'both buns',1)
    cmd.load_cgo(obj_diff1,'set1 - set2',1)
    cmd.load_cgo(obj_diff2,'set2 - set1',1)


cmd.extend("buried_unsats_from_logfile", buried_unsats_from_logfile )
cmd.extend("contrast_unsats_logfile", contrast_unsats_logfile )
