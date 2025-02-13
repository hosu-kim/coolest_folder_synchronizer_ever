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
import os
import sys
from pathlib import Path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts import FolderSynchronizer
from scripts import SyncConfig

class TestFolderSynchronizer:
    @pytest.fixture
    def temp_dirs(self):
        """Create temporary directories for testing"""
        with tempfile.TemporaryDirectory() as source_dir, \
             tempfile.TemporaryDirectory() as replica_dir, \
             tempfile.NamedTemporaryFile(suffix='.log') as log_file:
                yield source_dir, replica_dir, log_file.name

    def test_basic_sync(self, temp_dirs):
        """Test basic file synchronization"""
        source_dir, replica_dir, log_path = temp_dirs

        # Create test file
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

        # Verify synchronization
        replica_file = Path(replica_dir) / "test.txt"
        assert replica_file.exists()
        assert replica_file.read_text() == "test content"

    def text_nested_sync(self, temp_dirs):
        """Test nested directory synchronization"""
        source_dir, replica_dir, log_path = temp_dirs

        # Create nested directories and file
        nested_dir = Path(source_dir) / "foler1" / "folder2"
        nested_dir.mkdir(parents=True)
        nested_file = nested_dir / "nested.txt"
        nested_file.write_text("nested content")

        config = SyncConfig(
            source_path=Path(source_dir),
            replica_path=Path(replica_dir),
            log_path=Path(log_path),
            interval=60
        )

        sync = FolderSynchronizer(config)
        sync.sync_folders()

        # Verify nested synchronization
        replica_file = Path(replica_dir) / "folder1" / "folder2" / "nested.txt"
        assert replica_file.exists()
        assert replica_file.read_text() == "nested content"

def test_file_deletion(self, temp_dirs):
    """test file deletion synchronization"""
    source_dir, replica_dir, log_path = temp_dirs

    # Initial file creation and sync
    source_file = Path(source_dir) / "delete_me.txt"
    source_file.write_text("temporary content")

    config = SyncConfig(
        source_path=Path(source_dir),
        replica_path=Path(replica_dir),
        log_path=Path(log_path),
        interval=60
    )

    sync = FolderSynchronizer(config)
    sync.sync_folder()

    # Verify deletion
    replica_file = Path(replica_dir) / "delete_me.txt"
    assert not replica_file.exists()
