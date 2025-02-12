import pytest
from pathlib import Path
from folder_sync import FolderSynchronizer

def test_file_hash_calculation(temp_path):
    """Create test file"""
    test_file = temp_path / "test.txt"
    test_file.write_text("test centent")

    sync = FolderSynchronizer(str(temp_path), str(temp_path / "replica"), "test.log", 60)
    hash1 = sync.calculate_file_hash(test_file)
    hash2 = sync.calculate_file_hash(test_file)

    assert hash1 == hash2

    

