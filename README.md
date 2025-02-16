<p align="center">
  <img src="images/logo.png" width="300">
</p>

# Coolest Folder Synchronizer ever!
This tool automatically keeps an exact copy of a source folder in a different location, continuously checking for changes and recording all actions in detailed logs. Think of it as an automated backup system that ensures your replica folder always matches the original.
## Installation
Clone the repository:
```zsh
git clone https://github.com/hosu-kim/coolest_folder_synchronizer.git
```
Install the package:
```zsh
pip install .
```
## Usage
Run the program using the following command:
```zsh
folder-sync <source_path> <replica_path> <log_path> <interval>
```
### Parameters
- `source_path`: Path to the source folder to be synchronized
- `replica_path`: Path where the replica will be maintained
- `log_path`: Path where the log file will be created
- `interval`: Synchronization interval in seconds
### Example
```zsh
folder-sync /path/to/source /path/to/replica /var/log/sync.log 60
```
## Project Structure
```code
.
├── LICENSE
├── README.md
├── images
│   └── logo.png
├── src
│   ├── __init__.py
│   ├── config.py
│   ├── folder_sync.py
│   ├── input_validation.py
│   ├── resource_management.py
│   └── scripts
│       └── __init__.py
├── setup.py
└── tests
    ├── __init__.py
    └── test_folder_sync.py
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
