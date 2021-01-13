from sys import version
from setuptools import setup

setup(
    name='coinprice-cli',
    version='0.1.0',
    packages=['coinprice'],
    entry_points={
        'console_scripts': [
            'coinprice = coinprice.__main__:main'
        ]
    }
)
