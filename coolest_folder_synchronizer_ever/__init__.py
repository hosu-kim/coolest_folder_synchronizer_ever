r"""
 __     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Coolest Folder Synchronizer
==========================

A tool for synchronizing folders with logging and validation.

Created: 2025-02-13 21:45:28 UTC+1
Author: Hosu Kim
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