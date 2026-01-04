import os
import shutil
import argparse
import yaml
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%H:%M:%S')

def load_config(config_path):
    """Loads sorting rules from a YAML file."""
    if not Path(config_path).exists():
        logging.error(f"Config file not found: {config_path}")
        return None
    
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def get_destination_folder(extension, rules):
    """Determines the folder name based on the file extension."""
    for folder, extensions in rules['rules'].items():
        if extension.lower() in extensions:
            return folder
    return "Others"

def unique_path(directory, filename):
    """Creates a unique path to avoid overwriting existing files."""
    counter = 1
    path = directory / filename
    while path.exists():
        stem = path.stem
        suffix = path.suffix
        # If file exists, append a number: document_1.pdf
        path = directory / f"{stem}_{counter}{suffix}"
        counter += 1
    return path

def organize_files(target_dir, config_path):
    """Main logic to organize files."""
    target_path = Path(target_dir)
    
    if not target_path.exists():
        logging.error(f"Target directory does not exist: {target_dir}")
        return

    config = load_config(config_path)
    if not config:
        return

    logging.info(f"📂 Starting organization of: {target_path}")

    # Iterate over files in the directory
    for file in target_path.iterdir():
        if file.is_file() and file.name != "config.yaml" and not file.name.startswith('.'):
            # 1. Determine destination
            folder_name = get_destination_folder(file.suffix, config)
            destination_dir = target_path / folder_name
            
            # 2. Create folder if it doesn't exist
            destination_dir.mkdir(exist_ok=True)
            
            # 3. Move file safely
            new_path = unique_path(destination_dir, file.name)
            shutil.move(str(file), str(new_path))
            
            logging.info(f"Moved: {file.name} -> {folder_name}/")

    logging.info("✅ Organization complete!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CLI Tool to organize files based on extensions.")
    
    # Argument: Target Directory
    parser.add_argument(
        "directory", 
        type=str, 
        nargs='?', 
        default=".", 
        help="Path to the directory you want to organize (default: current folder)"
    )
    
    # Argument: Config File
    parser.add_argument(
        "--config", 
        type=str, 
        default="config.yaml", 
        help="Path to the configuration YAML file"
    )

    args = parser.parse_args()
    
    organize_files(args.directory, args.config)
