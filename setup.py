import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="wappdriver",
    version="0.2.5",
    license='MIT',
    author="Aahnik Daw",
    author_email="meet.aahnik@gmail.com",
    description="A package that automates sending messages through WhatsApp Web ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aahnik/wappdriver",
    install_requires=['selenium', 'pyyaml', 'requests'],
    packages=setuptools.find_packages(),
    package_data={'wappdriver': ['data/*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
