
from distutils.core import setup

setup(
    name='gitio',
    version='1.0',
    description='Create short GitHub URLs from the terminal',
    author='Siddharth Dushantha',
    author_email='siddharth.dushantha@gmail.com',
    url='https://github.com/sdushantha/gitio',
    entry_points = {
        'console_scripts': ['gitio=gitio:main'],
    }
)