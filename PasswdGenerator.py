import secrets, random, string, sys

class PasswdGenerator(object):

    def __init__(self):
        '''Constructor'''
        # Strings of unique characters (to avoid similar-looking ones)
        self.__uniLoC = 'abcdefghijkmnopqrstuvwxyz'
        self.__uniUpC = 'ABCDEFGHJKLMNPRSTUVWXYZ'
        self.__uniDig = '23456789'
        self.__uniSpc = '!#%+:=?@_/\\'

        # Passwords list
        self.__passwds=[]

    @property
    def Passwds(self):
        return self.__passwds
    @Passwds.setter
    def Passwds(self, newPasswds):
        if not isinstance(newPasswds, list):
            raise TypeError('Expected list, got' + str(type(newPasswds)))
        self.__passwds=newPasswds


    def Generate(self, l=32, n=1, uc=True, lc=True, dg=True, sp=False, uni=False, nod=False):
        '''Generate list of n passwords of l length each.

        uc (True) - Allow use of UpperCase letters
        lc (True) - Allow use of LowerCase letters
        dg (True) - Allow use of Digits
        sp (False) - Allow use of Special Characters
        uni (False) - Disallow use of similarly looking characters
        nod (False) - Disallow duplicate characters
        '''
        chars = ''

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
            self.Passwds.append(p)

        return p


    def Evaluate(self, passwds):
        '''Conduct evaluation of passwords'''
        raise NotImplementedError


    def Print(self):
        '''Print list of generated passwords'''
        if not self.Passwds:
            print('No Passwords generated')
        else:
            for i, item in enumerate(self.Passwds):
                print(str(i+1)+')\t'+str(item))


    def Clear(self):
        self.Passwds = []