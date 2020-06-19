import argparse, sys, gui, tkinter as tk
from PasswdGen import PasswdGen

__version__ = '0.2.0'

argv = argparse.ArgumentParser(description='Generate secure random passwords', epilog='Version '+__version__+' Marek "Saligia" Bialoruski, 2020')

# String Arguments
argv.add_argument('-n', type=str, help='number of passwords to be generated Default: 10', default=10)
argv.add_argument('-l', type=str, help='length of passwords to be generated Default: 20', default=20)

# Boolean Arguments
argv.add_argument('-uc', action='store_true', help='use UpperCase letters Default: On', default=True)
argv.add_argument('-lc', action='store_true', help='use LowerCase letters Default: On', default=True)
argv.add_argument('-dg', action='store_true', help='use Digits Default: On', default=True)
argv.add_argument('-sp', action='store_true', help='use special characters Default: Off')
argv.add_argument('-uni', action='store_true', help='disallow similar characters Default: On', default=True)
argv.add_argument('-nod', action='store_true', help='disallow duplicate characters Default: Off')
argv.add_argument('-w', '--window', action='store_true', help='enable GUI mode Default: Off')

# Parse Arguments
cArgs = argv.parse_args()


def main(cArgs):

    # GUI Code with Tkinter
    if cArgs.window:
        root = tk.Tk()
        # root.minsize(800, 600)
        root.title('Python3 Password Generator v.'+__version__+' GUI Mode')
        app = gui.Application(root, cArgs)
        app.mainloop()

        return None

    if cArgs.n <= 0:
        print('Please provide number of passwords greater than 0')
        return None
    if cArgs.l <= 0:
        print('Please provide password length greater than 0')
        return None

    try:
        pg = PasswdGen()
        pg.Generate(cArgs.l, cArgs.n, cArgs.uc, cArgs.lc, cArgs.dg, cArgs.sp, cArgs.uni)
        pg.Print()
        pg.Clear()
    except ValueError:
        print('Error, check arguments and try again')
        return None

    return None

if __name__ == "__main__": sys.exit(main(cArgs) or 0)