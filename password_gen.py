from random import choice
import argparse
import string

arg = argparse.ArgumentParser(add_help=True)
arg.add_argument('-s', '--size', default=20, nargs="?", type=int, help='Parameter to set size of password you will generate')
arg.add_argument('-q', '--quantity', default=10, nargs="?", type=int, help="Parameter to set how much passwords you want to generate each time you run the script")
arg.add_argument('-n', '--numbers', nargs="?", const=True, default=False, help='Parameter to set just numbers in the password')
arg.add_argument('-l', '--letters', nargs="?", const=True, default=False, help='Parameter to set just letters in the password')
arguments = arg.parse_args()

def password_generator(args):
    if args.numbers:
        password_chars = (list(string.digits))
    elif args.letters:
        password_chars = (list(string.ascii_letters))
    else:
        password_chars = (list(string.digits) * 3) + (list(string.ascii_letters) * 3) + list(string.punctuation)
    password = ""
    for char in range(args.size):
        password += choice(password_chars)
    return password

for passwd_number in range(arguments.quantity):
    print(password_generator(arguments))
