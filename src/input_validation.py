r"""
 __     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Coolest Folder Synchronizer Ever
==========================

Input validation utilities for the Coolest Folder Synchronizer.

This module provides validation functions for paths and synchronization intervals.

Created: 2025-02-13 20:11:12 UTC
Author: Hosu Kim
"""
import os
from pathlib import Path

def validate_paths(source_path: Path, replica_path: Path, log_path: Path) -> None:
    """Validates source, replica and log paths for synchronization.

    Args:
        source_path: Path to the source directory to be synchronized
        replica_path: Path to the replica directory for synchronization
        log_path: Path where synchronization logs will be written

    Raises:
        ValueError: If any of the following conditions are met:
            - Source path does not exist
            - Source and replica paths are identical
            - No write permision for replica path
            - Log directory does not exist
    """
    if not source_path.exists():
        raise ValueError(f"Source path does not exist: {source_path}")

    if source_path == replica_path:
        raise ValueError("Source and replica paths cannot be the same.")

    if replica_path.exists() and not os.access(replica_path, os.W_OK):
        raise ValueError(f"No write permission for replica path: {replica_path}")

    log_dir = log_path.parent
    if not log_dir.exists():
        raise ValueError(f"Log directory does not exist: {log_dir}")

def validate_interval(interval: int) -> None:
    """Validates the synchronization interval.

    Args:
        interval: Time in seconds between synchronization operations

    Raises:
        ValueError: If interval is not a positive integer
    """
    if interval <= 0:
        raise ValueError(f"Invalied interval: {interval}. Must be positive.")
