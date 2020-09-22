'''
# For Developers Only
- Run WappDriver without having to pip install
- Test changes instantaneously 
- WappDriver is a package, so running files directly will lead to all sorts of import errors
- Just trust on Pylance and this runner to make sure whether the imports you are making are correct or not

'''

from wappdriver.__init__ import __version__, error

print(__version__)

