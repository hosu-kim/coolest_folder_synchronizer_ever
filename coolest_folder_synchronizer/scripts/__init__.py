r"""
 __     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Coolest Folder Synchronizer
==========================

Core functionality modules for the Coolest Folder Synchronizer.

This package provides the main components for folder synchronization:
    * FolderSynchronizer: Main synchronization implementation
    * SyncConfig: Configuration management
    * ResourceManager: Resource handling and cleanup

Created: 2025-02-13 21:44:03 UTC+1
Author: Hosu Kim
"""

from .folder_sync import FolderSynchronizer
from .config import SyncConfig
from .resource_management import ResourceManager  # manage_resources 대신 ResourceManager

__all__ = [
    'FolderSynchronizer',
    'SyncConfig',
    'ResourceManager'
]