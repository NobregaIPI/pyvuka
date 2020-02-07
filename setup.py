import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyVuka", # Replace with your own username
    version="0.1.8",
    author="R Paul Nobrega",
    author_email="Paul@PaulNobrega.net",
    description="General Purpose Global Data Analysis Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bostonautolytics/pyvuka",
    packages=setuptools.find_packages(),
    install_requires=["asteval>=0.9.18", "chardet>=3.0.4", "lmfit>=1.0.0", "matplotlib>=3.1.3", "numpy>=1.18.1",
                      "pack64>=2.0.1", "Pillow>=7.0.0", "psutil>=5.6.7", "PyQt5>=5.14.1", "scipy>=1.3.1",
                      "xlrd>=1.2.0", "XlsxWriter>=1.2.7"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Free For Educational Use",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)