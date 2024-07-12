from setuptools import setup

setup(
    name='skfxdev-cli',
    version=__import__('sd_cli').__version__,
    url='https://skfx.dev',
    author='GAMch1k',
    long_description='Крутая программа! Very cool program!',
    entry_points={
        'console_scripts':
            ['sd = sd_cli.cli:main']
    }
)
