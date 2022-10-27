import time as t
from random import randint


def sPrint(*args, lowercase:bool = False, uppercase:bool = False, capitalise:bool = False, alternating:bool = False, obfuscate:bool = False, bold:bool = False):
    if sum([lowercase,uppercase,capitalise,alternating]) > 1:
        raise ValueError("Recieved illegal parameters")
    out = []
    for count, i in enumerate(args):
        out.append(str(args[count]))
    out = ''.join(out)
    if lowercase: out = out.lower()
    elif uppercase: out = out.upper()
    elif capitalise: out = out.title()
    elif alternating: out = ''.join([x.lower() if i%2 else x.upper() for i,x in enumerate(out)])
    elif obfuscate:
        alphabet = list(map(chr, range(97, 123)))
        out = list(out)
        for letter in range(len(out)):
            if randint(0,1) == 1:
                out[letter] = alphabet[randint(0,25)]
            else:
                out[letter] = alphabet[randint(0, 25)].upper()
        out = ''.join(out)
    else: out = str(''.join(out))
    if not bold: print(out)
    else: print("\033[1m"+out+"\033[1m")





class Debug:
    @staticmethod
    def timeFunction(func):
        def wrapper(*args):
            base = t.time() #Take time before execution
            func(*args) #Execute passed function
            print("Function {} took {} seconds to execute".format(func.__name__, t.time() - base))
        return wrapper



@Debug.timeFunction
def sayHi(name:str = 'PyCharm'):
    sPrint(f'Hi, {name}')


if __name__ == '__main__':
    sayHi('PyCharm')
