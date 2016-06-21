'''
Available in colorama

Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL

'''

from colorama import init
from colorama import Fore, Back, Style
init()

def switch(x):
    return {
        'black': Fore.BLACK,
        'red': Fore.RED,
        'green': Fore.GREEN,
        'yellow': Fore.YELLOW,
        'blue': Fore.BLUE,
        'magenta': Fore.MAGENTA,
        'cyan': Fore.CYAN,
        'white': Fore.WHITE,
        'reset': Fore.RESET
    }[x]

def dbg( msg, ident=None, clr=None ):
    m = msg
    if ident:
        m = ident + ":" + msg
    if clr:
        m = switch(clr) + m + Style.RESET_ALL

    print m
