from pymol.cgo import *
from pymol import cmd

obj = []
white =  [ COLOR, 1.0, 1.0, 1.0 ]
blue = [ COLOR, 0.0, 0.0, 1.0 ]
red  = [ COLOR, 1.0, 0.0, 0.0 ]

for line in open( "test.kin" ).readlines() :
    cols = line.strip().split()
    if len(cols) == 0 : continue
    if cols[0] == "@dotlist" :
        for j in xrange(len(cols)) :
            if cols[ j ] == "color=" :
                if cols[j+1] == "red" :
                    obj.extend( red )
                elif cols[j+1] == "blue" :
                    obj.extend( blue )
                else :
                    obj.extend( white )
    if cols[0] == "{dot}" :
        obj.extend( [ SPHERE, float(cols[2]), float(cols[3]), float(cols[4]), 0.05 ] )

cmd.load_cgo(obj,'test',1)


