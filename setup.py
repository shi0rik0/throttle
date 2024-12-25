from setuptools import setup, find_packages

setup(
    name='throttle',
    version='0.0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    author='shi0rik0',
    description=
    'Provides a rate limiter to throttle the execution of some code.',
)
