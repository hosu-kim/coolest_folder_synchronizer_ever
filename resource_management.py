class FolderSynchronizer:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
    """Cleanup code here"""
    logging.info("Synchronization stopped.")

    def cleanup(self):
    """Additional cleanup if needed"""
    pass
	