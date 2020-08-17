#!/bin/bash

echo -e  "\n \t Make sure to READ ALL INSTRUCTIONS before running this script  😊  \n "
echo -e "\t https://gist.github.com/aahnik/5e473000fb3ac24ef0251a52c5f45473#file-upload_to_pypi-md  \n "
echo -e  "You can ctrl + click (cmd on mac) on the url or copy and paste it in your browser \n\n "
echo -e "Make sure to execute this script from the root directory of the project,"
echo -e "i.e the same directory which contains setup.py \n "

read -p "Press ENTER to continue "

rm -r *.egg-info build dist 
python3 -m pip install --user --upgrade setuptools wheel
python3 setup.py sdist bdist_wheel
python3 -m pip install --user --upgrade twine
twine upload dist/*

# AAHNIK 2020 