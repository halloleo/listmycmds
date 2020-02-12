"""
Minimal setup for listmycmds
"""

DEPENDENCIES = ['argh']

from setuptools import setup, find_packages
setup(name='listmycmds',
    version='1.0',
    py_modules=['listmycmds_for_setup', 'listmycmds'],
    entry_points={'console_scripts': ['listmycmds=listmycmds_for_setup:main']},
    install_requires=DEPENDENCIES
    )
