from setuptools import setup

setup(
    name='vivida',
    version='0.0.1',
    author='Elias Bachaalany',
    author_email='elias.bachaalany@gmail.com',
    packages=['vivida'],
    scripts=[],
    url='',
    license='LICENSE.txt',
    description='vivida, an IDAPython bridge for vivisect',
    long_description='',
    install_requires=['vivisect'],
    entry_points={
        'console_scripts': [
            'vivida=vivida.main:main'
        ]
    }
)    