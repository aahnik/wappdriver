from . import __version__
import argparse

try:
    from pyfiglet import Figlet
except:
    print('''Could not find pyfiglet
            Run 
                pip install pyfiglet
        ''')



def main():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    print(f'wappdriver: {__version__}')
    f = Figlet(font='big')
    print(f.renderText('wappdriver'))



if __name__ == "__main__":
    main()
