r"""
__     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Coolest Folder Synchronizer
==========================

Test suite for the Coolest Folder Synchronizer.

This modlue contains tests that verify the core functionality of the folder
synchronization system, including basic operations, nested directory handling,
and file deletion synchronization.

Created: 2025-02-13 20:49:29 UTC
Author: Hosu Kim
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
    """Test suite for FolderSynchronizer class.

    This test suite verifies the core functionality of the FolderSynchronizer,
    including file creation, nested directory handling, and deletion synchronization.
    """
    @pytest.fixture
    def temp_dirs(self):
        """Create temporary directories for testing
        
        Creates three temporary locations:
            - Source directory for original files
            - Replica directory for synchronized files
            - Log file for tracking operations

        Yields:
            tuple: Contains (source_dir, replica_dir, log_file_path)
        """
        with tempfile.TemporaryDirectory() as source_dir, \
             tempfile.TemporaryDirectory() as replica_dir, \
             tempfile.NamedTemporaryFile(suffix='.log') as log_file:
                yield source_dir, replica_dir, log_file.name

    def test_basic_sync(self, temp_dirs):
        """Tests basic file synchronization functionality.

        Verifies that a single file is correctly synchronized from source
        to replica directory.

        Args:
            temp_dirs: Fixture providing temporary test directories

        Tests:
            1. File creation in source directory
            2. Synchronization to replica directory
            3. Content verification between source and replica
        """
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

    def test_nested_sync(self, temp_dirs):
        """Test nested directory synchronization

        Verifies that files in nested directory structures are correctly
        synchronized while maintaining the directory hierarchy.
        
        Args:
            temp_dirs: Fixture providing temporary test directories

        Tests:
            1. Nested directory creation
            2. File creation in nested directory
            3. Directory structure replication
            4. Content verification in nested structure
        """
        source_dir, replica_dir, log_path = temp_dirs

        # Create nested directories and file
        nested_dir = Path(source_dir) / "folder1" / "folder2"
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
        """Test file deletion synchronization

        Verifies that file deletions in the source directory are correctly
        propagated to the replica directory.
        
        Args:
            temp_dirs: Fixture providing temporary test directories

        Tests:
            1. Initial file creation and sync
            2. File deletion in source
            3. Deletion synchronization to replica
            4. Verification of file removal
        """
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
        sync.sync_folders()

        source_file.unlink()
        sync.sync_folders()

        # Verify deletion
        replica_file = Path(replica_dir) / "delete_me.txt"
        assert not replica_file.exists()
