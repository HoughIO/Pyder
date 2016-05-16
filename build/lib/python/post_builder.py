from main import *
import os
import time

class Post():
  """A post generator for Pyder, a static blog generator"""
  
  def __init__(self, title, author):
    """Initialize attributes on a post-to-post basis. This consists of generating a dir with the date, then the name of the post."""
    self.title = title

    currentDate = str(time.strftime("%d.%m.%Y"))
    self.genDate = currentDate

    self.author = author.upper()
    
    os.mkdir('posts/' + self.genDate)
    fileTitle = self.title.lower()[0:15].replace(" ", "_")
    f = open(('posts/' + self.genDate + fileTitle + '.md'), 'w')

    content = ''
    content += str("#" + self.title + "\n\n")
    content += str("###### By " + self.author + "\n\n")
    f.write(content)

