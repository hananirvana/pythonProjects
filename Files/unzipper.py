import zipfile
import os

def extract_folders_flat(zip_file_path, extract_to_dir):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for member in zip_ref.namelist():
            # Extract the file info
            file_info = zip_ref.getinfo(member)

            # Check if the member is a directory
            if not file_info.is_dir():
                # Extract to the target directory, flattening the path
                target_path = os.path.join(extract_to_dir, os.path.basename(member))

                # Create the directory if it doesn't exist
                os.makedirs(os.path.dirname(target_path), exist_ok=True)

                # Extract the file
                with zip_ref.open(member) as source, open(target_path, 'wb') as target:
                    target.write(source.read())
            else:
                # If it's a directory, just create it in the target directory
                os.makedirs(os.path.join(extract_to_dir, os.path.basename(member)), exist_ok=True)

# Example usage
extract_folders_flat('my_archive.zip', 'here')
