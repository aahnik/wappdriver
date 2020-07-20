import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="wapp",
    version="0.0.1",
    license='MIT',
    author="Aahnik Daw",
    author_email="aahnikdaw@gmail.com",
    description="A package that automates WhatsApp Web ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aahnik/wapp",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)

