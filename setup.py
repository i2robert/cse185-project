import os
from setuptools import setup, find_packages

# version-keeping code based on pybedtools
curdir = os.path.abspath(os.path.dirname(__file__))
MAJ = 0
MIN = 2
REV = 4
VERSION = '%d.%d.%d' % (MAJ, MIN, REV)
with open(os.path.join(curdir, 'segno/version.py'), 'w') as fout:
        fout.write(
            "\n".join(["",
                       "# THIS FILE IS GENERATED FROM SETUP.PY",
                       "version = '{version}'",
                       "__version__ = version"]).format(version=VERSION)
        )


setup(
    name='segno',
    version=VERSION,
    description='a fastq file quality-based trimmer',
    author='Isaac Roberts',
    author_email='i2robert@ucsd.edu',
    install_requires=[
        'fastq',
        'miniFasta'
    ],
    packages=find_packages(include=['segno']),
    entry_points={
        "console_scripts": [
            "segno=segno.segno:main"
        ],
    },
)