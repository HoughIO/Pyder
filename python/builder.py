import os
import shutil
import sys

class Site():

  """A simple python website generator."""

  def __init__(self, name):
    """Initialize name attributes."""
    self.name = name
    # this gets the directory builder.py is running in, and chops off '/python/builder.py'
    self.pyderPath = os.path.realpath(__file__)[0:-18]

  def config(self):
    """A config generator based on inputted params"""
    self.firstName = input("First Name: ")
    self.lastName = input("Last Name: ")
    self.email = input("Email: ")
    self.twitter = input("Twitter @: ")
    self.title = input("Site Title: ")
    self.domain = input("Domain: ")
    self.theme = "default"

  def noConfigDraw(self):
    """Creates config.yml, but does not ask for input"""
    self.firstName = ''
    self.lastName = ''
    self.email = ''
    self.twitter = ''
    self.title = ''
    self.domain = ''
    self.theme = "default"
    
    open(self.name + "/config.yml", 'a').close()

  def configDraw(self):
    """Creates the config.yml file and saves it."""
    output = ''

    output += str("FirstName:\n\t" + self.firstName + "\n\n")
    output += str("LastName:\n\t" + self.lastName + "\n\n")
    output += str("Email:\n\t" + self.email + "\n\n")
    output += str("Twitter:\n\t" + self.twitter + "\n\n")
    output += str("Title:\n\t" + self.title + "\n\n")
    output += str("Domain:\n\t" + self.domain + "\n\n")
    output += str("Theme:\n\t" + self.theme + "\n\n")

    f = open(self.name + '/config.yml', 'w')
    f.write(output)

  def directoryDraw(self):
    os.mkdir(self.name)
    os.mkdir(self.name + '/posts')
    os.mkdir(self.name + '/_site')
    # copy default pages and themes from pyder into the site
    print("Copying site defaults from " + self.pyderPath)
    shutil.copytree(self.pyderPath + '/default/pages/', self.name + '/pages')
    shutil.copytree(self.pyderPath + '/default/themes/', self.name + '/themes')
    os.mkdir(self.name + '/img')

  # generate html from the site's theme, the pages, and the posts.
  # put site into _site directory.
  def siteDraw(self):
    html = []
    token = os.getcwd().split('/').pop()
    if token != self.name:
      print("You must be in your site's root directory to generate HTML.")
      return
    themePath = str(os.getcwd() + '/themes/' + self.theme + '/')
    with open(str(themePath) + "/head.html", "r") as head:
      for line in head:
        html.append(line)
    html.append("<body>")
    with open(str(themePath + '/header.html'), "r") as header:
      for line in header:
        html.append(line)
    with open(str(themePath + '/body.html'), "r") as body:
      for line in body:
        html.append(line)
    with open(str(themePath + "/footer.html"), "r") as footer:
      for line in footer:
        html.append(line)
    html.append("</body>")
    html.append("</html>")
    f = open("_site/index.html", "w")
    for item in html:
      f.write(str(item + "\n"))
    f.close()
    shutil.copytree(themePath + '/css', os.getcwd() + '/_site/css')
    shutil.copytree(themePath + '/js', os.getcwd() + '/_site/js')
    shutil.copytree(themePath + '/font', os.getcwd() + '/_site/font')
    
