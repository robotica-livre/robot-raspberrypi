#!/usr/bin/env python
""" Robot Raspberry Pi setup module """

from setuptools import setup

pkgname = "robot-raspberrypi"
version = "0.0.1"

install_requires = [
    "",
]

tests_require = [
    "pytest",
]

metadata = {
    "name": pkgname,
    "version": version,
    "author": "Ricardo M. Oliveira",
    "author_email": "ricardo.martinelli.oliveira@gmail.com",
    "url": "http://github.com/robotica-livre/robot-raspberrypi",
    "description": "",
    "include_package_data": True,
    "install_requires": install_requires,
    "tests_require": tests_require
}

setup(**metadata)