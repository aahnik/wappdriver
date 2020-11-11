'''
command line
'''


from . import __version__
import argparse
from . import local


from pyfiglet import Figlet



def main():
    '''
    The command line parser for 
    '''
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print(f'''
    wappdriver: {__version__} 

    wappdriver is `wa` on command line

    To know usage : wa --usage

    For help : wa --help

    ''')
    f = Figlet(font='big')
    print(f.renderText('wappdriver'))


def wa():
    parser = argparse.ArgumentParser()
    parser.add_('send',
                        help=''' 

                        '''
                        )
    args = parser.parse_args()


if __name__ == "__main__":
    main()
