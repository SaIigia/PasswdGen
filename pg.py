import argparse, sys
from PasswdGenerator import PasswdGenerator

argv = argparse.ArgumentParser(description='Generate random passwords')

# Integer Arguments
argv.add_argument('-n', type=int, help='Number of passwords to be generated', default=0)
argv.add_argument('-l', type=int, help='Length of passwords to be generated', default=0)

# Boolean Arguments
argv.add_argument('-uc', action='store_true', help='Use UpperCase letters', default=True)
argv.add_argument('-lc', action='store_true', help='Use LowerCase letters', default=True)
argv.add_argument('-dg', action='store_true', help='Use digits', default=True)
argv.add_argument('-sp', action='store_true', help='Use special characters')
argv.add_argument('-uni', action='store_true', help='Disallow similar characters', default=True)
argv.add_argument('-nod', action='store_true', help='Disallow duplicate characters')

cArgs = argv.parse_args()

def main(cArgs):

    if cArgs.n <= 0: raise ValueError('Please provide number of passwords greater than 0')
    if cArgs.l <= 0: raise ValueError('Please provide length of passwords greater than 0')

    pg = PasswdGenerator()
    pg.Generate(cArgs.l, cArgs.n, cArgs.uc, cArgs.lc, cArgs.dg, cArgs.sp, cArgs.uni)
    pg.Print()

    return None

if __name__ == "__main__": sys.exit(main(cArgs) or 0)