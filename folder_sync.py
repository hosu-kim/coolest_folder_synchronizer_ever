"""
 __     __                             __  __  _   _                    
 \ \   / /___   ___   __ _  _ __ ___   \ \/ / | | | |  ___   ___  _   _ 
  \ \ / // _ \ / _ \ / _` || '_ ` _ \   \  /  | |_| | / _ \ / __|| | | |
   \ V /|  __/|  __/| (_| || | | | | |  /  \  |  _  || (_) |\__ \| |_| |
    \_/  \___| \___| \__,_||_| |_| |_| /_/\_\ |_| |_| \___/ |___/ \__,_|

Folder Synchronization Tool
---------------------------
File: folder_sync.py
Created: 12-02-2025
Author: Hosu Kim
Description: One-way folder synchronization utility that maintains an exact replica of
             a source folder. Performs periodic synchronization with loggig.
Usage:
    python folder_sync.py <source_path> <replica_path> <log_path> <interval>

Example:
    python folder_sync.py /source /replica /var/log/sync.log 60 
			 
Copyright (c) 2025 hosu-kim. All rights reserved.
"""
import os
import sys
import shutil
import hashlib
import logging
from pathlib import Path
import time
from typing import Optional

class FolderSynchronizer:
	def	__init__(self, source_path: str, replica_path: str, log_path: str, interval: int):
		self.source_path = Path(source_path)
		self.replica_path = Path(replica_path)
		self.interval = interval

		self.setup_logging(log_path)
	
	def	setup_logging(self, log_path: str) -> None:
		logging.basicConfig(
			level = logging.INFO,
			format = '%(asctime)s - %(message)s',
			handlers = [
				logging.FileHandler(log_path),
				logging.StreamHandler()
			]
		)
	
	def calculate_file_hash(self, file_path: Path) -> str:
		hash_md5 = hashlib.md5()
		with open(file_path, "rb") as f:
			for chunk in iter(lambda: f.read(4096), b""):
				hash_md5.update(chunk)
		return hash_md5.hexdigest()

	def sync_folders(self) -> None:
		try:
			self.replica_path.mkdir(parents=True, exist_ok=True)
			
			source_files = set()
			for path in self.source_path.rglob("*"):
				if path.is_file():
					relative_path = path.relative_to(self.source_path)
					source_files.add(relative_path)
					self.sync_file(relative_path)
			
			for path in self.replica_path.rglob("*"):
				if path.is_file():
					relative_path = path.relative_to(self.replica_path)
					if relative_path not in source_files:
						path.unlink()
						logging.info(f"Deleted: {path}")
		except Exception as e:
			logging.error(f"Synchronization error: {str(e)}")

	def sync_file(self, relative_path: Path) -> None:
		source_file = self.source_path / relative_path
		replica_file = self.replica_path / relative_path

		replica_file.parent.mkdir(parents=True, exist_ok=True)

		if not replica_file.exists() or \
			self.calculate_file_hash(source_file) != self.calculate_file_hash(replica_file):
				shutil.copy2(source_file, replica_file)
				logging.info(f"Copied: {source_file} -> {replica_file}")
	
	def run(self) -> None:
		logging.info("Starting folder synchronization")
		while True:
			self.sync_folders()
			logging.info(f"Synchronization completed. Waiting {self.interval} seconds...")
			time.sleep(self.interval)

def main():
	if len(sys.argv) != 5:
		print("Usage: python folder_sync.py <source_path> <replica_path> <log_path> <interval>")
		sys.exit(1)

	source_path = sys.argv[1]
	replica_path = sys.argv[2]
	log_path = sys.argv[3]
	interval = int(sys.argv[4])

	synchronizer = FolderSynchronizer(source_path, replica_path, log_path, interval)
	synchronizer.run()

if __name__ == "__main__":
	main()