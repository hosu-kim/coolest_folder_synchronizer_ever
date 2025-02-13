r"""
__     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Coolest Folder Synchronizer
---------------------------
File: test_folder_sync.py
Created: 12-02-2025
Author: Hosu Kim
Description: Test cases for folder synchronization
"""
import pytest
import tempfile
from pathlib import Path

from scripts.folder_sync import FolderSynchronizer
from scripts.config import SyncConfig

class TestFolderSynchronizer:
    @pytest.fixture
    def temp_dirs(self):
        with tempfile.TemporaryDirectory() as source_dir, \
             tempfile.TemporaryDirectory() as replica_dir, \
             tempfile.NamedTemporaryFile(suffix='.log') as log_file:
                yield source_dir, replica_dir, log_file.name

    def test_basic_sync(self, temp_dirs):
        source_dir, replica_dir, log_path = temp_dirs

        """Create test file"""
        source_file = Path(source_dir) / "test.txt"
        source_file.write_text("test content")

        config = SyncConfig(
            source_path=Path(source_dir),
            replica_path=Path(replica_dir),
            log_path=Path(log_path),
            interval=60
        )

        sync = FolderSynchronizer(config)
        sync.sync_folders()

        """Verify synchronization"""
        replica_file = Path(replica_dir) / "test.txt"
        assert replica_file.exists()
        assert replica_file.read_text() == "test content"
