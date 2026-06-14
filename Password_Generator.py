import random
import string

try:
    length = int(input("Please enter the length of your desired password."))

except ValueError:
    print("Please enter a valid number.")
    raise SystemExit(1)


if length in range(4):
    print("Sorry, Passwords can only be of 4+ digits :(")
    raise SystemExit(1)

charecters = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range (length):
    password += random.choice(charecters)

print("Generated Password:", password)