import setuptools
import re

with open(".github/pypi.md", "r") as f:
    long_description = f.read()

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('wappdriver/__init__.py', 'r').read(),
    re.M).group(1)

setuptools.setup(
    name="wappdriver",
    version=version,
    license='MIT',
    author="Aahnik Daw",
    author_email="meet.aahnik@gmail.com",
    description="A package that automates sending messages through WhatsApp Web ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aahnik/wappdriver",
    install_requires=['selenium', 'pyyaml', 'requests', 'pyfiglet', 'tqdm'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['wappdriver=wappdriver.command_line:main'],
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
