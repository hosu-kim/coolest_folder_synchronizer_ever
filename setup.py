r"""
 __     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Coolest Folder Synchronizer
---------------------------
File: setup.py
Created: 13-02-2025
Author: Hosu Kim
"""

from setuptools import setup, find_packages

setup(
	name="cooliest_folder_synchronizer",
	version="0.1",
	author="Hosu Kim",
	author_email="hosu@outlook.cz",
	description="folder Synchronizer",
	packages=find_packages(),
	install_requites=[
		"pytest",
	],
	python_requites=">=3.10",
	classifiers=[
		"Development status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"License :: OSI approved :: MIT Licnese",
		"Programming Language :: Python :: 3.10",
	],
)