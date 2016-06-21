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

def back_switch(x):
    return {
        'black': Back.BLACK,
        'red': Back.RED,
        'green': Back.GREEN,
        'yellow': Back.YELLOW,
        'blue': Back.BLUE,
        'magenta': Back.MAGENTA,
        'cyan': Back.CYAN,
        'white': Back.WHITE,
        'reset': Back.RESET
    }[x]

def dbg( msg, ident=None, clr=None ):
    m = msg
    if ident:
        m = ident + ":" + msg
        if clr:
            m = back_switch(clr) + Style.BRIGHT + Fore.BLACK + ident +":" + Style.RESET_ALL + msg
    elif clr:
        m = switch(clr) + m + Style.RESET_ALL

    print m
