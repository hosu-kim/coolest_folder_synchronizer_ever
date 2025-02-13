r"""
 __     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Coolest Folder Synchronizer
---------------------------
File: __init__.py
Created: 13-02-2025
Author: Hosu Kim
"""
"""
Coolest Folder Synchronizer
--------------------------
A tool for synchronizing folders with logging and validation.
"""

__version__ = "0.1.0"
__author__ = "Hosu Kim"

from .scripts.folder_sync import FolderSynchronizer
from .scripts.config import SyncConfig
from .scripts.resource_management import ResourceManager

__all__ = [
    'FolderSynchronizer',
    'SyncConfig',
    'ResourceManager'
]