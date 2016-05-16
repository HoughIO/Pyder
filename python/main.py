import sys
#from .site import Site

#For refrence, line 6 lists the number of arguments by calling for the length of the arguemnt list.
#Line 7 prints the list of objects as a refrenceable string.
#print('Number of arguements: ', len(sys.argv), 'arguemnts')
#print('Argument List:', str(sys.argv))

# Example Syntax for Pyder:
# Pyder new STRING
# 
# This will generate a new blog site and call Site.config()

# Example syntax for a new post using Pyder:
# Pyder post STRING
#
# In this case, Pyder will generate a new post, resync the
# generated HTML files. STRING is the post's title.

if len(sys.argv) == 3:
  arg1 = str(sys.argv[1])
  arg2 = str(sys.argv[2])
else:
  print("Incorrect arguments, please refer to the docs.")

if 'arg1' in locals() and 'arg2' in locals() and arg1 == "new":
  projectTitle = arg2
  print('New blog will be generated as ' + str(arg2))
