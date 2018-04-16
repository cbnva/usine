"Minimalist remote tasks execution via SSH."
from codecs import open  # To use a consistent encoding
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

VERSION = (0, 1, 0)

__author__ = 'Pyrates'
__contact__ = "yohan.boniface@data.gouv.fr"
__homepage__ = "https://github.com/pyrates/usine"
__version__ = ".".join(map(str, VERSION))

setup(
    name='usine',
    version=__version__,
    description=__doc__,
    long_description=long_description,
    url=__homepage__,
    author=__author__,
    author_email=__contact__,
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='ssh deployment',
    packages=find_packages(exclude=['tests']),
    extras_require={'test': ['pytest'], 'docs': 'mkdocs'},
    include_package_data=True,
)
