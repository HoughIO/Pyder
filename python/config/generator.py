def main():
  output = ''

  firstName = input("What is your first name?")
  lastName = input("What is your last name?")
  email = input("What is your email?")
  twitter = input("What is your twitter @?")
  customDomain = input("Are you using a custom domain? No or domain name.")
  theme = "Default"

  output += str("FirstName:\n\t" + firstName + "\n")
  output += str("LastName:\n\t" + lastName + "\n")
  output += str("Email:\n\t" + email + "\n")
  output += str("twitter:\n\t" + twitter + "\n")
  if customDomain == "n" or customDomain == "No" or customDomain == "N":
    output += str("Domain:\n\tFalse\n")
  else:
    output += str("Domain:\n\t" + customDomain + "\n")
  output += str("Theme:\n\t" + theme + "\n")

  f = open('../config', 'w')
  f.write(output)


main()
