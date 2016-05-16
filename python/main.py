import sys
from builder import *

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

def help():
  print("""
    Hello! Welcome to Pyder.
    Usage:
      Pyder new STRING
        Where STRING is the title of your site.
      
      Pyder help
        Prints these docs

    Flag options:
      --no-config       
        Generates the site without prompting to fill out a config.yml file.

    @2016 Graham Hough, Ethan Miller
    """)
  sys.exit()

if len(sys.argv) == 2:
  if str(sys.argv[1]).title() == "Help":
    print(help())
  if str(sys.argv[1]).title() == "H":
    print(help())

elif len(sys.argv) == 3:
  if str(sys.argv[1]).title() != "Post" and str(sys.argv[1]).title() != "New":
    print(help())
  else:
    arg1 = str(sys.argv[1])

  arg2 = str(sys.argv[2])

elif len(sys.argv) == 4:
  if str(sys.argv[1]).title() != "Post" and str(sys.argv[1]).title() != "New":
    print(help())
  else:
    arg1 = str(sys.argv[1])

  arg2 = str(sys.argv[2])
  if str(sys.argv[3]) == "--no-config":
    arg3 = str(sys.argv[3])
  else:
    print("Invalid flag option")
    print(help())
else:
  print("Incorrect arguments, please refer to the docs.")
  print(help())

if 'arg1' in locals() and 'arg2' in locals() and arg1 == "new":
  projectTitle = arg2
  print('New blog will be generated as ' + str(arg2))
  newSite = Site(str(arg2))
  newSite.directoryDraw()
  if 'arg3' in locals() and arg3 == '--no-config':
    print("Please fill out config.yml in your sites directory")
    newSite.noConfigDraw()
    newSite.configDraw()
  else:
    newSite.config()
    newSite.configDraw()
