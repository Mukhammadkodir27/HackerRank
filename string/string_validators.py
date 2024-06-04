# String Validators

if __name__ == '__main__':
    string = input()

# Check for alphanumeric characters
    print(any(c.isalnum() for c in string))

# Check for alphabetical characters
    print(any(c.isalpha() for c in string))

# Check for digits
    print(any(c.isdigit() for c in string))

# Check for lowercase characters
    print(any(c.islower() for c in string))

# Check for uppercase characters
    print(any(c.isupper() for c in string))


"""
str.isalnum()
This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

str.isalpha()
This method checks if all the characters of a string are alphabetical (a-z and A-Z).

str.isdigit()
This method checks if all the characters of a string are digits (0-9).

str.islower()
This method checks if all the characters of a string are lowercase characters (a-z).

str.isupper()
This method checks if all the characters of a string are uppercase characters (A-Z).
"""
