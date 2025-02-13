"""
Core functionality modules for the Coolest Folder Synchronizer.
"""

from .folder_sync import FolderSynchronizer
from .config import SyncConfig
from .resource_management import ResourceManager  # manage_resources 대신 ResourceManager

__all__ = [
    'FolderSynchronizer',
    'SyncConfig',
    'ResourceManager'
]