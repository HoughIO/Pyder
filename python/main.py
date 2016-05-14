import os

class Site():

  """A simple python website generator."""

  def __init__(self, name):
    """Initialize name attributes."""
    self.name = name

  def config(self):
    """A config generator based on inputted params"""
    self.firstName = input("First Name: ")
    self.lastName = input("Last Name: ")
    self.email = input("Email: ")
    self.twitter = input("Twitter @: ")
    self.title = input("Site Title: ")
    self.domain = input("Domain: ")
    self.theme = "default"

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

    f = open('../_site/config.yml', 'w')
    f.write(output)

  def directoryDraw(self):
    os.mkdir(self.name)
    os.mkdir(self.name + '/posts')
    os.mkdir(self.name + '/_site')
    os.mkdir(self.name + '/themes/')
    os.mkdir(self.name + '/themes/default')
    os.mkdir(self.name + '/themes/default/css')
    os.mkdir(self.name + '/themes/default/js')
    os.mkdir(self.name + '/pages')
    os.mkdir(self.name + '/img')

