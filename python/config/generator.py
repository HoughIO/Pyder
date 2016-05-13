def main():
  output = ''

  firstName = input("What is your first name: ")
  lastName = input("What is your last name: ")
  email = input("What is your email: ")
  twitter = input("What is your twitter @: ")
  customDomain = input("Are you using a custom domain \(string or \"No\"\): ")
  theme = "Default"

  output += str("FirstName:\n\t" + firstName + "\n\n")
  output += str("LastName:\n\t" + lastName + "\n\n")
  output += str("Email:\n\t" + email + "\n\n")
  output += str("twitter:\n\t" + twitter + "\n\n")
  if customDomain == "n" or customDomain == "No" or customDomain == "N":
    output += str("Domain:\n\tFalse\n\n")
  else:
    output += str("Domain:\n\t" + customDomain + "\n\n")
  output += str("Theme:\n\t" + theme + "\n\n")

  f = open('../../config.yml', 'w')
  f.write(output)


main()
