import os
import time

class Post():
  """A post generator for Pyder, a static blog generator"""
  
  def __init__(self, title):
    """Initialize attributes on a post-to-post basis. This consists of generating a dir with the date, then the name of the post."""
    self.title = title
    self.fileTitle = self.title.lower()[0:15].replace(" ", "_")

    self.pwd = os.getcwd()
    self.dirContents = os.listdir()

    self.genDate = str(time.strftime("%d.%m.%Y"))

    self.postsMadeToday = os.path.exists(os.getcwd() + '/posts/' + self.genDate)

    if self.postsMadeToday == True:
      f = open(('posts/' + self.genDate + '/' + self.fileTitle + '.md'), 'w')
      content = ''
      content += str("#" + self.title + "\n\n")
      f.write(content)
    else:
      os.mkdir('posts/' + self.genDate)
      f = open(('posts/' + self.genDate + '/' + self.fileTitle + '.md'), 'w')
      content = ''
      content += str("#" + self.title + "\n\n")
      f.write(content)

