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
    
if __name__ == "__main__":
    main()
