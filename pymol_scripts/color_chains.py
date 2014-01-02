#####################################################################
#
# Colour by object-chain
#
#####################################################################
 
from pymol import cmd
 
def color_chains(rainbow=0):
 
        """
 
AUTHOR 

        Kevin Houlihan
        adapted from a script by Gareth Stockwell
 
USAGE
 
        color_chains(rainbow=0)
 
        This function colours each object currently in the PyMOL heirarchy
        with a different colour.  Colours used are either the 22 named
        colours used by PyMOL (in which case the 23rd object, if it exists,
        gets the same colour as the first), or are the colours of the rainbow
 
SEE ALSO
 
        util.color_objs()
        """
 
        # Process arguments
        rainbow = int(rainbow)
 
        # Get names of all PyMOL objects
        # obj_list = cmd.get_names('objects')
	# don't color selections, alignments, measurements, etc.
	obj_list = cmd.get_names_of_type("object:molecule")
	chain_list = []
	for obj in obj_list:
		for ch in cmd.get_chains(obj):
			# there seems to be a bug in pymol, some CA don't get colored
			#sele = obj + " and c. " + ch + " and (e. C or name CA)"
			#sele = obj + " and c. " + ch + " and e. C"
			sele = obj + " and c. " + ch
			chain_list.append(sele)
 
        if rainbow:
 
           #print "\nColouring objects as rainbow\n"
 
           nobj = len(obj_list)
	   nchain = len(chain_list)
 
           # Create colours starting at blue(240) to red(0), using intervals
           # of 240/(nobj-1)
           for j in range(nchain):
              # hsv = (240-j*240/(nobj-1), 1, 1)
	      # disparate colors for adjacent objects in sequence, colors heterodimers nicely
	      hsv = (240 - ( (120*(j - j%2))/(nchain-1) + 120*(j%2) ), 1, 1)
              # Convert to RGB
              rgb = hsv_to_rgb(hsv)
              # Define the new colour
              cmd.set_color("col" + str(j), rgb)
              #print chain_list[j], rgb
              # Colour the object
              cmd.color("col" + str(j), chain_list[j])
	      util.cnc(chain_list[j])
 
        else:
 
           #print "\nColouring objects using PyMOL defined colours\n"
 
           # List of available colours
	   # standard pymol colors, I like these better
	   # color sets listed at http://www.pymolwiki.org/index.php/Color_Values
	   mainset1_colours = ['carbon', 'cyan', 'lightmagenta', 'yellow', 'salmon', 'hydrogen', 'slate', 'orange']
	   mainset2_colours = ['lime', 'deepteal', 'hotpink', 'yelloworange', 'violetpurple', 'grey70', 'marine', 'olive']
	   mainset3_colours = ['smudge', 'teal', 'dirtyviolet', 'wheat', 'deepsalmon', 'lightpink', 'aquamarine', 'paleyellow']
           mainset4_colours = ['limegreen', 'skyblue', 'warmpink', 'limon', 'violet', 'bluewhite', 'greencyan', 'sand']
	   mainset5_colours = ['forest', 'lightteal', 'darksalmon', 'splitpea', 'raspberry', 'grey50', 'deepblue', 'brown']
	   #colours = mainset1_colours + mainset4_colours
	   colours = mainset1_colours + mainset2_colours + mainset3_colours + mainset4_colours + mainset5_colours
	   # colors in original script
           extra_colours = ['red', 'green', 'blue', 'yellow', 'violet', 'cyan',    \
           'salmon', 'lime', 'pink', 'slate', 'magenta', 'orange', 'marine', \
           'olive', 'purple', 'teal', 'forest', 'firebrick', 'chocolate',    \
           'wheat', 'white', 'grey' ]
           ncolours = len(colours)
 
           # Loop over objects
           i = 0
           for ch in chain_list:
              #print "  ", obj, ch, colours[i]
              cmd.color(colours[i], ch)
	      util.cnc(ch)
              i += 1
	      i %= ncolours
 
# HSV to RGB routine taken from Robert L. Campbell's color_b.py script
#   See http://pldserver1.biochem.queensu.ca/~rlc/work/pymol/
# Original algorithm from: http://www.cs.rit.edu/~ncs/color/t_convert.html
def hsv_to_rgb(hsv):
 
        h = float(hsv[0])
        s = float(hsv[1])
        v = float(hsv[2])
 
        if( s == 0 ) :
                #achromatic (grey)
                r = g = b = v
 
        else:
                # sector 0 to 5
                h = h/60.            
                i = int(h)
                f = h - i                       # factorial part of h
                p = v * ( 1 - s )
                q = v * ( 1 - s * f )
                t = v * ( 1 - s * ( 1 - f ) )
 
                if i == 0:
                        (r,g,b) = (v,t,p)
                elif i == 1:
                        (r,g,b) = (q,v,p)
                elif i == 2:
                        (r,g,b) = (p,v,t)
                elif i == 3:
                        (r,g,b) = (p,q,v)
                elif i == 4:
                        (r,g,b) = (t,p,v)
                elif i == 5:
                        (r,g,b) = (v,p,q)
                else:
                        (r,g,b) = (v,v,v)
                        print "error, i not equal 1-5"
 
        return [r,g,b]
 
 
 
# Add color_chains to the PyMOL command list 
cmd.extend("color_chains",color_chains)

#cmd.auto_arg[0]["color_chains"] = [ cmd.object_sc, "object", '']
