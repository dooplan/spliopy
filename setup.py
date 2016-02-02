# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding

setup(
    name='spliopy',
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.1.2',
    description='Python wrapper around the API, using Splio API REST 1.0',
    # The project's main homepage.
    url='https://github.com/dooplan/spliopy',
    author='Pasqual Guerrero',
    author_email='pasqual.guerrero@gmail.com',
    license='MIT',
    packages=find_packages(),
)
