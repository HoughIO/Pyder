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
    self.theme = input("Theme (blank for default): ")

example = Site('Creamy Memes for Depressing Teens')
example.config()
