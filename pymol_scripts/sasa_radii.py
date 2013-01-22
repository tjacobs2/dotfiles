import pymol
from pymol import cmd

def show_SASA_radii_expanded_polars(sel="all"):
   cmd.alter(sel+" and element C", "vdw=3.40") # 2.00 + 1.4
   cmd.alter(sel+" and element N", "vdw=4.15") # 1.75 + 1.4 + 1.0
   cmd.alter(sel+" and element O", "vdw=3.95") # 1.55 + 1.4 + 1.0
   cmd.alter(sel+" and element H", "vdw=2.40") # 1.00 + 1.4
   cmd.alter(sel+" and element P", "vdw=3.55") # 2.15 + 1.4
   cmd.alter(sel+" and element S", "vdw=3.30") # 1.90 + 1.4
   cmd.set("sphere_scale", 1.0)

def show_SASA_radii(sel="all"):
   cmd.alter(sel+" and element C", "vdw=3.40") # 2.00 + 1.4
   cmd.alter(sel+" and element N", "vdw=3.15") # 1.75 + 1.4
   cmd.alter(sel+" and element O", "vdw=2.95") # 1.55 + 1.4
   cmd.alter(sel+" and element H", "vdw=2.40") # 1.00 + 1.4
   cmd.alter(sel+" and element P", "vdw=3.55") # 2.15 + 1.4
   cmd.alter(sel+" and element S", "vdw=3.30") # 1.90 + 1.4
   cmd.set("sphere_scale", 1.0)

def show_Rosetta_radii(sel="all"):
   cmd.alter(sel+" and element C", "vdw=2.00")
   cmd.alter(sel+" and element N", "vdw=1.75")
   cmd.alter(sel+" and element O", "vdw=1.55")
   cmd.alter(sel+" and element H", "vdw=1.00")
   cmd.alter(sel+" and element P", "vdw=2.15")
   cmd.alter(sel+" and element S", "vdw=1.90")
   cmd.set("sphere_scale", 1.0)

cmd.extend('show_SASA_radii_expanded_polars',show_SASA_radii_expanded_polars)
cmd.extend('show_SASA_radii',show_SASA_radii)
cmd.extend('show_Rosetta_radii',show_Rosetta_radii)

