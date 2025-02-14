# Coolest Folder Synchronizer ever!
This tool automatically keeps an exact copy of a source folder in a different location, continuously checking for changes and recording all actions in detailed logs. Think of it as an automated backup system that ensures your replica folder always matches the original.
## Installation
Clone the repository
```zsh
git clone https://github.com/hosu-kim/coolest_folder_synchronizer.git
```
## Usage
Run the program using the following command:
```zsh
python3 scripts/folder_sync.py <source_path> <replica_path> <log_path> <interval>
```
### Parameters
- `source_path`: Path to the source folder to be synchronized
- `replica_path`: Path where the replica will be maintained
- `log_path`: Path where the log file will be created
- `interval`: Synchronization interval in seconds
### Example
```zsh
python3 scripts/folder_sync.py /path/to/source /path/to/replica /var/log/sync.log 60
```
## Project Structure
```code
.
├── LICENSE                              # MIT License
├── setup.py                             # Package setup and installation
├── docs/
│   └── README.md                        # Documentation
├── coolest_folder_synchronizer_ever/    # Main package directory
│   ├── __init__.py                      # Package initialization
│   ├── scripts/                         # Core functionality
│   │   ├── __init__.py
│   │   ├── config.py                    # Configuration management
│   │   ├── folder_sync.py               # Main synchronization logic
│   │   ├── input_validation.py          # Input validation utilities
│   │   └── resource_management.py       # Resource management utilities
│   └── tests/                           # Test directory
│       ├── __init__.py
│       └── test_folder_sync.py          # Test cases
```
## Testing
The project includes a comprehensive test suite. 

To run the tests:
```zsh
pytest tests/test_folder_sync.py
```
### Test Coverage
- Basic synchronization functionality
- File creation, modification, and deletion
- Error handling and retry mechanism
- Edge cases and invalid inputs
## Logging
The tool provides detailed logging of all operations:
- File copies
- File deletions
- Hash verification results
- Errors and retry attempts
- Synchronization completion status
Example log output:
```code
2025-02-12 18:28:26 UTC - INFO - Starting folder synchronization
2025-02-12 18:28:26 UTC - INFO - Copied: /source/file.txt -> /replica/file.txt
2025-02-12 18:28:27 UTC - INFO - Synchronization completed. Waiting 60 seconds...
```
## Error Handling
The tool implements several error handling mechanisms:
- Validates all input parameters
- Verifies file system permissions
- Implements retry logic for failed operations
- Provides detailed error messages
- Ensures clean program termination

## Performance Considerations
- Uses efficient file comparison through MD5 hashing
- Implements buffered file reading for large files
- Minimizes unnecessary file operations
- Optimized for both small and large directory structures
## Limitations
- One-way synchronization only
- Does not handle symbolic links
- No real-time event monitoring (uses polling)
- Limited to file systems accessible through Python's standard library
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
## License
This project is licensed under the MIT License - see the LICENSE file for details.
## Author
hosu-kim
## Support
For support, please create an issue in the GitHub repository or contact me directly.
