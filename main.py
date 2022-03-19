import random
import string


# modify the following parameter to generate passwords with unique characters
require_unique = False

# the main function that generates pseudo-random passwords using the random module
def generate_pwd():
    upper = random.choices(string.ascii_uppercase, k=5)
    lower = random.choices(string.ascii_lowercase, k=5)
    digits = random.choices(string.digits, k=5)
    symbols = random.choices(['@', '%', '$', '!', '#', '{', '}', '(', ')', '[', ']',
         '.', ',', ':', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~'], k=5)

    combined = random.choices(upper + lower + digits + symbols, k=8)
    random.shuffle(combined)

    return ''.join(combined)


# the recursive function to generate passwords with all unique characters
def unique_generator(pwd = generate_pwd()):
    for character in pwd:
        if not pwd.count(character) == 1:
            _ = generate_pwd()
            return(unique_generator(_))
    else:
        return(pwd)


# the main code
final = unique_generator() if require_unique else generate_pwd()
print(final)
