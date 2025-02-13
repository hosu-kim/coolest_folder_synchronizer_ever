r"""
 __     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Coolest Folder Synchronizer
==========================

Configuration management for folder synchronization.

This module provides configuration settings for the folder synchronization
utility through a dataclass-based configuration.

Created: 2025-02-13 21:36:18 UTC+1
Author: Hosu Kim
"""
from dataclasses import dataclass
from pathlib import Path

@dataclass
class SyncConfig:
    """Configuration settings for folder synchronization.

    Attributes:
        source_path: Path to the source directory to be synchronized
        replica_path: Path to the replica directory for synchronization
        log_path: Path where synchronization logs will be written
        inteval: Time in seconds between synchronization operations
        chunk_size: Size of chunks when reading files for hash calculation
        max_retires: Maximum number of retry appempts for failed operations
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    source_path: Path
    replica_path: Path
    log_path: Path
    interval: int

# Additional configuration options with default values
    chunk_size: int = 4096  # Default chunk size for file reading
    max_retries: int = 3    # Default number of retry attempts
    log_level: str = "INFO" # Default logging level
