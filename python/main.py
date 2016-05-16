import sys
from .site import Site

print('Number of arguements: ', len(sys.argv), 'arguemnts')
print('Argument List:', str(sys.argv))

newSite = Site("test")

newSite.config()
