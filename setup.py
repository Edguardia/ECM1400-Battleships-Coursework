import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="battleships-pkg-epratt",
    version="1.0.0",
    author="Edward Pratt",
    author_email="ep718@exeter.ac.uk",
    description="A battleships game built for the module ECM1400 at the University of Exeter.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Edguardia/ECM1400-Battleships-Coursework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
    ],
    python_requires='>=3.11'
)