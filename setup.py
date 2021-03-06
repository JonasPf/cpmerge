from __future__ import with_statement
from setuptools import setup

from cpmerge import cpmerge

classifiers = [
    "Programming Language :: Python :: 2.7",
    "Intended Audience :: End Users/Desktop",
    "License :: OSI Approved :: MIT License",
    "Operating System :: POSIX :: Linux",
    "Topic :: Utilities",
    "Environment :: X11 Applications"
]

with open("README", "r") as fp:
    long_description = fp.read()

setup(name="cpmerge",
      version=cpmerge.__version__,
      author="Jonas Pfannschmidt",
      author_email="jonas.pfannschmidt@gmail.com",
      url="http://jonaspfannschmidt.com/cpmerge",
      packages=['cpmerge'],
      package_data={'cpmerge': ['icon.png']},
      description="A simple clipboard manager to synchronize the CLIPBOARD and PRIMARY selection under linux",
      long_description=long_description,
      license="MIT",
      classifiers=classifiers,
      install_requires=['docopt'],
      entry_points={'console_scripts': ['cpmerge = cpmerge.cpmerge:main']},
      )
