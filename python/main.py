import sys
from builder import *
from post_builder import *

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

def findCallType(argument):
  argument.pop(0)
  if len(argument) == 2:
    if argument[0].title() == 'New':
      newSite = Site(argument[1])
      newSite.directoryDraw()
      newSite.config()
      newSite.configDraw()
    elif argument[0].title() == 'Post':
      newPost = Post(argument[1])
    else:
      print(help())
  elif len(arguments) == 3:
      if argument[2] == "--no-config":
        newSite = Site(argument[1])
        newSite.directoryDraw()
        newSite.noConfigDraw()
        newSite.configDraw()
        print("Please fill out config.yml in your sites directory")
  else:
    print(help())


argument = sys.argv
findCallType(argument)
