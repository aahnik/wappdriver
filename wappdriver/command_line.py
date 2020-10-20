from . import __version__
import argparse

try:
    from pyfiglet import Figlet
except Exception:
    print('''Could not find pyfiglet
            Run 
                pip install pyfiglet
        ''')


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
    parser.add_argument('send',
                        help=''' 

                        '''
                        )
    args = parser.parse_args()


if __name__ == "__main__":
    main()
