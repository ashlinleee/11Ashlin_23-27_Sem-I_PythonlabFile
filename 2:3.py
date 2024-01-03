email = input("Enter an email address: ")
username, _, domain = email.partition("@")
email_tuple = (username, domain)
print("Tuple of username and domain:", email_tuple)
