import os
import time

class Post():
  """A post generator for Pyder, a static blog generator"""
  
  def __init__(self, title, author):
    """Initialize attributes on a post-to-post basis. This consists of generating a dir with the date, then the name of the post."""
    self.title = title
    self.fileTitle = self.title.lower()[0:15].replace(" ", "_")

    self.pwd = os.getcwd()
    self.dirContents = os.listdir()

    self.genDate = str(time.strftime("%d.%m.%Y"))

    self.author = author.title()

    self.postsMadeToday = os.path.exists(os.getcwd() + '/posts/' + self.genDate)

    if postsMadeToday == True:
      f = open(('posts/' + self.genDate + fileTitle + '.md'), 'w')
      content = ''
      content += str("#" + self.title + "\n\n")
      content += str("###### By " + self.author + "\n\n")
      f.write(content)
    else:
      os.mkdir('posts/' + self.genDate)
      f = open(('posts/' + self.genDate + fileTitle + '.md'), 'w')
      content = ''
      content += str("#" + self.title + "\n\n")
      content += str("###### By " + self.author + "\n\n")
      f.write(content)

