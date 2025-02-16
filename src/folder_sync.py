r"""
 __     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Coolest Folder Synchronizer Ever
==========================

One-way folder synchronization utility.

This module provides functionality to maintain an exact replica of a source folder
through periodic synchronization with logging capabilities.

Example:
    >>> config = SyncConfig(
    ...     source_path=Path("/source"),
    ...     replica_path=Path("/replica"),
    ...     log_path=Path("/var/log/sync.log"),
    ...     interval=60
    ... )
    >>> with FolderSynchroizer(config) as sync:
    ...     sync.run()

Created: 2025-02-13 20:19:54 UTC
Author: Hosu Kim
"""

import sys
import shutil
import hashlib
import logging
import time
from pathlib import Path
from typing import Set

from .config import SyncConfig
from .input_validation import validate_paths, validate_interval
from .resource_management import ResourceManager

class FolderSynchronizer(ResourceManager):
    """Manages one-way folder synchronization with logging.
    
    Maintains an exact replica of a source folder by performing periodic
    synchronization with configurable intervals and logging.

    Attributes:
        config: Configuration settings for synchronization
        source_path: Path to the source directory
        replica_path: Path to the replica directory
        interval: Time between synchronizations in seconds
        running: Flag indicating if synchronization is active
    """
    def __init__(self, config: SyncConfig):
        """Initializes the folder synchronizer.
        
        Args:
            config: Configuration settings for the synchronization
        """
        self.config = config
        self.source_path = config.source_path
        self.replica_path = config.replica_path
        self.interval = config.interval
        self.running = False

        self.setup_logging(config.log_path)
        validate_paths(config.source_path, config.replica_path, config.log_path)
        validate_interval(config.interval)

    def setup_logging(self, log_path:Path) -> None:
        """Configures logging for synchronization operations.

        Args:
            log_path: Path where log files will be written
        """
        logging.basicConfig(
            level=getattr(logging, self.config.log_level),
            format='%(asctime)s UTC = %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_path),
                logging.StreamHandler()
            ]
        )

    def calculate_file_hash(self, file_path: Path) -> str:
        """Calculates MD5 hash of a file.

        Args:
            file_path: Path to the file to hash

        Returns:
            str: MD5 hash of the file

        Raises:
            IOError: If file reading fails
        """
        hash_md5 = hashlib.md5()
        try:
            with open(file_path, "rb") as f:
                for chunk in iter(lambda: f.read(self.config.chunk_size), b""):
                    hash_md5.update(chunk)
            return hash_md5.hexdigest()
        except IOError as e:
            logging.error(f"Error calculating hash for {file_path}: {e}")
            raise

    def get_source_files(self) -> Set[Path]:
        """Gets set of all files in source directory.

        Returns:
            Set[Path]: Set of relative paths for all files in source directory
        """
        return {path.relative_to(self.source_path)
                for path in self.source_path.rglob("*")
                if path.is_file()}

    def sync_file(self, relative_path: Path, retry_count: int=0) -> None:
        """Synchronizes a single file from source to replica.

        Args:
            relative_path: Path of file relative to source directory
            retry_count: Number of pervious retry attempts

        Raises:
            Exception: If synchronization fails after max retries
        """
        source_file = self.source_path / relative_path # '/': Path joining operator with pathlib.Path
        replica_file = self.replica_path / relative_path

        try:
            replica_file.parent.mkdir(parents=True, exist_ok=True)
            
            if not replica_file.exists() or \
                self.calculate_file_hash(source_file) != self.calculate_file_hash(replica_file):
                    shutil.copy2(source_file, replica_file)
                    logging.info(f"Copied: {source_file} -> {replica_file}")
        except Exception as e:
            if retry_count < self.config.max_retries:
                logging.warning(f"Retry {retry_count + 1} for {source_file}")
                time.sleep(1)
                self.sync_file(relative_path, retry_count + 1)
            else:
                logging.error(f"Failed to sync {source_file} after {self.config.max_retries} retries: {e}")
                raise

    def sync_folders(self) -> None:
        """Performs one complete synchronization of folders.

        Raises:
            Exception: If synchronization encounters an error
        """
        try:
            self.replica_path.mkdir(parents=True, exist_ok=True)
            source_files = self.get_source_files()
            
            for relative_path in source_files:
                self.sync_file(relative_path)

            for path in self.replica_path.rglob("*"):
                if path.is_file():
                    relative_path = path.relative_to(self.replica_path)
                    if relative_path not in source_files:
                        path.unlink()
                        logging.info(f"Deleted: {path}")
        
        except Exception as e:
            logging.error(f"Synchronization error: {str(e)}")
            raise

    def run(self) -> None:
        """Starts continuous folder synchronization.

        Synchronizes folders periodically until interrupted.
        """
        logging.info("Starting folder synchronization.")
        self.running = True

        try:
            while self.running:
                self.sync_folders()
                logging.info(f"Synchronization completed. Waiting {self.interval} seconds...")
                time.sleep(self.interval)
        except KeyboardInterrupt:
            logging.info("Synchronization stopped by user")
        except Exception as e:
            logging.error(f"Fatal error: {e}")
            raise

def main():
    """Command-line entry point for folder synchronization.

    Usage:
        python3 folder_sync.py <source_path> <replica_path> <log_path> <inteval>

    Returns:
        int: Exit code (0 for success, 1 for error)
    """
    if len(sys.argv) != 5:
        print("Usage: python folder_sync.py <source_path> <replica_path> <log_path> <interval>")
        sys.exit(1)

    try:
        config = SyncConfig(
            source_path=Path(sys.argv[1]),
            replica_path=Path(sys.argv[2]),
            log_path=Path(sys.argv[3]),
            interval=int(sys.argv[4])
        )

        with FolderSynchronizer(config) as sync:
            sync.run()

    except ValueError as e:
        print(f"Configuration error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
