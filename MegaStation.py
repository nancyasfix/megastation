import os
import shutil
import json

class MegaStation:
    def __init__(self, storage_path):
        self.storage_path = storage_path
        self.data_index = {}

    def analyze_storage(self):
        """Analyzes the data storage and updates the data index."""
        self.data_index.clear()
        for root, dirs, files in os.walk(self.storage_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                self.data_index[file_path] = file_size
        print("Storage analysis complete.")
        return self.data_index

    def manage_storage(self, max_storage_bytes):
        """Manages the storage to ensure it does not exceed the specified limit."""
        total_size = sum(self.data_index.values())
        if total_size <= max_storage_bytes:
            print("Current storage is within the limit.")
            return

        sorted_files = sorted(self.data_index.items(), key=lambda item: item[1], reverse=True)

        print(f"Total storage exceeds limit by {total_size - max_storage_bytes} bytes. Starting cleanup...")
        for file_path, file_size in sorted_files:
            if total_size <= max_storage_bytes:
                break
            try:
                os.remove(file_path)
                total_size -= file_size
                print(f"Removed {file_path}, freed {file_size} bytes.")
            except OSError as e:
                print(f"Error removing {file_path}: {e}")

    def export_data_index(self, output_file):
        """Exports the data index to a JSON file."""
        with open(output_file, 'w') as f:
            json.dump(self.data_index, f, indent=4)
        print(f"Data index exported to {output_file}.")

    def import_data_index(self, input_file):
        """Imports the data index from a JSON file."""
        with open(input_file, 'r') as f:
            self.data_index = json.load(f)
        print(f"Data index imported from {input_file}.")

# Example usage
if __name__ == "__main__":
    storage_path = "C:\\path\\to\\your\\storage"
    max_storage_bytes = 50 * 1024 * 1024  # 50 MB

    mega_station = MegaStation(storage_path)
    mega_station.analyze_storage()
    mega_station.manage_storage(max_storage_bytes)
    mega_station.export_data_index("data_index.json")