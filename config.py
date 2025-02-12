"""
 __     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Coolest Folder Synchronizer
---------------------------
File: config.py
Created: 12-02-2025
Author: Hosu Kim
Description: Configuration management for folder synchronization
"""
from dataclasses import dataclass
from pathlib import Path

@dataclass
class Syncconfig:
    source_path: Path
    replica_path: Path
    log_path: Path
    interval: int

    """Additional configuration options"""
    chunk_size: int = 4096
    max_retries: int = 3
    log_level: str = "INFO"
