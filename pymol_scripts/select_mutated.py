#! /usr/bin/env python

from pymol import cmd

def select_mutated(obj1,obj2,sele2=None):
  """
DESCRIPTION

  "select_mutated" finds and selects the amino acid differences in the second object when compared to the first object. 
  It highlights the mutations in yellow sticks for easy identification. This new function can also handle length changes 
  by using PyMOL's built-in align method.

  Some parts of this script were taken from a similar script written by Christoph Malisi, located on the PyMOL wiki at 
  www.pymolwiki.org/index.php/Color_By_Mutations

USAGE 

  select_mutated wild_type_object_to_compare_to, mutant_object_to_select, selection_of_mutant_residues_to_limit_comparison_to

EXAMPLES

  select_mutated 1xuu, 1ame, 1ame and chain g + 1ame and chain h
  select_mutated 1xuu, *

  """
  if ( sele2 == None ):
    sele2 = obj2

  objects = cmd.get_names("objects")
  for o in objects:
    if o.startswith(obj2):
      obj2 = o
      break

  one_letter ={'VAL':'V', 'ILE':'I', 'LEU':'L', 'GLU':'E', 'GLN':'Q','ASP':'D', 'ASN':'N', 'HIS':'H', 'TRP':'W', 'PHE':'F', 'TYR':'Y',  \
               'ARG':'R', 'LYS':'K', 'SER':'S', 'THR':'T', 'MET':'M', 'ALA':'A','GLY':'G', 'PRO':'P', 'CYS':'C', 'MSE':'M', 'ASX':'N'  }

  print "select_mutated called with object 1: " + obj1 + " and object 2: " + obj2

  # use PyMOL to get a sequence alignment of the two objects (don't do any refinement to get a better fit - just align the sequences)
  cmd.align( obj2, obj1, object="alignment", cycles=0 )

  # after doing the sequence alignment, use super to do a sequence-independent, structure-based alignment. supposedly much better than align.
  cmd.super( obj2, obj1 )
  
  # alignment is an "object" which somehow contains both objects that were used for the alignment. we'll iterate over this alignment object
  # and save the chain, resi, and resn for each aligned position.  making the big assumption here that the order of elements in the alignment
  # object is the same for both actual aligned objects, which seems to be the case. 
  stored.obj1_resi = []
  stored.obj2_resi = []
  
  stored.obj1_resn = []
  stored.obj2_resn = []
  
  stored.obj1_chain = []
  stored.obj2_chain = []

  cmd.iterate( obj1 + " and n. CA and alignment", "stored.obj1_resi.append( resi )" )
  cmd.iterate( obj2 + " and n. CA and alignment", "stored.obj2_resi.append( resi )" )

  cmd.iterate( obj1 + " and n. CA and alignment", "stored.obj1_resn.append( resn )" )
  cmd.iterate( obj2 + " and n. CA and alignment", "stored.obj2_resn.append( resn )" )

  cmd.iterate( obj1 + " and n. CA and alignment", "stored.obj1_chain.append( chain )" )
  cmd.iterate( obj2 + " and n. CA and alignment", "stored.obj2_chain.append( chain )" )


  sele_mutations_list = []
  sele_insert_list = []
  wt_list = []
  mut_list = []
  mutations = []

  # loop over the aligned residues
  for resn1, resn2, resi1, resi2, ch1, ch2 in zip( stored.obj1_resn, stored.obj2_resn, stored.obj1_resi, stored.obj2_resi, stored.obj1_chain, stored.obj2_chain ):
    # take care of 'empty' chain names
    if ch1 == '':
      ch1 = '""'
    if ch2 == '':
      ch2 = '""'
    if resn1 != resn2:
      #print "%s/%s-%s => %s/%s-%s" % ( ch1, resn1, resi1, ch2, resn2, resi2 )
      sele_exp = '/' + '/'.join([ obj2, '', ch2, resi2 ])
      sele_mutations_list.append( sele_exp )
      
      wt_list.append( one_letter[resn1] )
      mut_list.append( one_letter[resn2] )
      mutations.append( "%s:%s%s%s" % ( ch2, one_letter[resn1], resi2, one_letter[resn2]) )

  if not mutations:
    print "No mutations found."
    return

  selename = "mutated-" + obj2
  #print "+".join(sele_mutations_list)
  cmd.select(selename, " + ".join(sele_mutations_list))
  print "Mutations found: '%s'" % (mutations)

  cmd.show("sticks", selename)
  hideexp = "(mutated-" + obj2 + " and hydro)"
  cmd.hide(hideexp)
  cmd.color( "yellow", selename + " and not (name N+CA+C+O)" )
  util.cnc(selename)
  cmd.disable(selename)

  for i in range(0,len(sele_mutations_list)):
    labelexp = '''"''' + wt_list[i] + '''%s''' + mut_list[i] + '''"''' + ''' % (resi)'''
    cmd.label( sele_mutations_list[i] + " and n. ca", labelexp )
    #labelexp = '''(name ca+C1*+C1' and (byres(mutated-''' + obj2 + ''')))'''
    #cmd.label(labelexp,'''"%s-%s"%(resn,resi)''')

  # identify insertions also, by using the mutated selection and alignment object
  # this will be the intersection of everything that's in object2 that's not in the alignment object (will included mutated positions and inserts) and 
  # not anything that's in the mutated selection
  selename = "inserts-" + obj2
  cmd.select( selename, "(" + obj2 + " and not hydro and !(" + obj2 + " in alignment)) and !(mutated-" + obj2 + ")" )
  cmd.color( "orange", selename )
  util.cnc(selename)
  cmd.disable(selename)

  # clean up after ourselves
  cmd.delete("alignment")

def select_mutated_all(refObj):
   for i in cmd.get_object_list():
       select_mutated(refObj,i)

cmd.extend("select_mutated",select_mutated)
cmd.extend("select_mutated_all",select_mutated_all)

