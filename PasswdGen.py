'''PasswdGen class file'''

import secrets, random, string, sys

class PasswdGen(object):
    '''Password generator object class. Allows generation of secure random passwords of arbitrary length.

    Usage:
        p = PasswdGen()
        p.Generate(args)

        to print: p.Print()
        to return list of passwords: p.Passwords

        When generating one password it can return that one with Generate() call
    '''

    def __init__(self):
        '''Constructor'''
        # Strings of unique characters (to avoid similar-looking ones)
        self.__uniLoC = 'abcdefghijkmnopqrstuvwxyz'
        self.__uniUpC = 'ABCDEFGHJKLMNPRSTUVWXYZ'
        self.__uniDig = '23456789'
        self.__uniSpc = '!#%+:=?@_/\\'

        # Passwords list
        self.__Passwords=[]

    @property
    def Passwords(self):
        return self.__Passwords
    @Passwords.setter
    def Passwords(self, nPasswords):
        if not isinstance(nPasswords, list):
            raise TypeError('Expected list, got' + str(type(nPasswords)))
        self.__Passwords=nPasswords


    def Generate(self, l=32, n=10, uc=True, lc=True, dg=True, sp=False, uni=False, nod=False):
        '''Generate list of n passwords of l length each.

        uc (True) - Allow use of UpperCase letters
        lc (True) - Allow use of LowerCase letters
        dg (True) - Allow use of Digits
        sp (False) - Allow use of Special Characters
        uni (False) - Disallow use of similarly looking characters
        nod (False) - Disallow duplicate characters
        '''
        chars = ''

        if isinstance(l, str): l = int(l)
        if isinstance(n, str): n = int(n)

        # Construct character string to pull from based on options given
        if uni:
            if uc: chars+=self.__uniUpC
            if lc: chars+=self.__uniLoC
            if dg: chars+=self.__uniDig
            if sp: chars+=self.__uniSpc
        else:
            if uc: chars+=string.ascii_uppercase
            if lc: chars+=string.ascii_lowercase
            if dg: chars+=string.digits
            if sp: chars+=string.punctuation

        # Check conditions
        if nod:
            if l > len(chars): raise ValueError('Too little characters for no duplicates !')
        if not chars: raise ValueError('No available characters !')

        # Shuffle available characters to increase randomness
        chars = list(chars)
        random.shuffle(chars)
        chars = ''.join(chars)

        # Generate passwords
        for _ in range(n):
            if nod: p = ''.join(random.sample(chars, l))
            else: p = ''.join(secrets.choice(chars) for j in range(l))
            self.Passwords.append(p)

        if n==1: return p


    def Print(self):
        '''Print list of generated passwords'''
        if not self.Passwords:
            print('No Passwords generated')
        else:
            for i, item in enumerate(self.Passwords):
                print(str(i+1)+')\t'+str(item))


    def PrintToString(self):
        if not self.Passwords:
            return 'No Passwords generated'
        else:
            pString = ''
            for i, item in enumerate(self.Passwords):
                pString+=(str(i+1)+')\t'+str(item)+'\n')
            return pString


    def Clear(self):
        '''Wipe contents of generated passwords list'''
        del self.__Passwords
        self.Passwords = []