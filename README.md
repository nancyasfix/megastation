# MegaStation

MegaStation is a Python-based utility designed to efficiently manage and analyze data storage on Windows systems. It utilizes advanced algorithms to provide insights into storage usage and ensures that storage limits are adhered to.

## Features

- **Analyze Storage:** Scans the specified storage directory and provides a detailed index of files and their sizes.
- **Manage Storage:** Automatically removes the largest files when storage exceeds a specified limit.
- **Export Data Index:** Saves the current data index to a JSON file for backup or analysis.
- **Import Data Index:** Loads a data index from a JSON file to continue from a previous state.

## Installation

Ensure you have Python 3.x installed on your Windows machine. Clone this repository and navigate to the folder where `MegaStation.py` is located.

## Usage

1. Set the `storage_path` variable to the path you want to analyze and manage.
2. Set the `max_storage_bytes` variable to your desired storage limit in bytes.
3. Run the script using the command:
   ```bash
   python MegaStation.py
   ```

## Example

```python
storage_path = "C:\\path\\to\\your\\storage"
max_storage_bytes = 50 * 1024 * 1024  # 50 MB

mega_station = MegaStation(storage_path)
mega_station.analyze_storage()
mega_station.manage_storage(max_storage_bytes)
mega_station.export_data_index("data_index.json")
```

## Contributing

Feel free to fork this repository, make changes, and create a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the LICENSE file for details.