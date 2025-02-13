r"""
 __     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Coolest Folder Synchronizer
==========================

Setup configuration for the Coolest Folder Synchronizer.

This module contains the package configuration and dependencies for the
Coolest Folder Synchronizer project. It provides:
    * Package metadata
    * Dependencies
    * Python version requirements
    * Project classifiers

Created: 2025-02-13 21::28 UTC
Author: Hosu Kim
"""

from setuptools import setup, find_packages

setup(
	name="coolest_folder_synchronizer",
	version="0.1",
	author="Hosu Kim",
	author_email="hosu@outlook.cz",
	description="A tool for synchronizing folders with logging and validation",
	packages=find_packages(),
	install_requires=[
		"pytest",
	],
	python_requires=">=3.10",
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3.10",
	],
)