# 🗂️ CLI File Organizer

A lightweight command-line tool written in Python that automates file management. It scans a target directory and organizes files into subfolders based on their extensions using a customizable YAML configuration.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![CLI](https://img.shields.io/badge/Interface-CLI-orange)
![Config](https://img.shields.io/badge/Config-YAML-green)

## 📌 Problem & Solution
**The Problem:** Downloads and Desktop folders often become cluttered with mixed file types (PDFs, images, installers), making it hard to find what you need.  
**The Solution:** A script that automatically sorts these files into logical categories (`Documents/`, `Images/`, `Archives/`) instantly.

## 🛠 Features
* **Customizable Rules:** Define your own folder mapping via `config.yaml`.
* **Safe Moving:** Automatically handles duplicate filenames (e.g., `image.png` -> `image_1.png`) to prevent data loss.
* **Cross-Platform:** Works on Windows, macOS, and Linux (powered by `pathlib`).
* **CLI Arguments:** Specify any target directory from the terminal.

## 🚀 Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/your-username/cli-file-organizer.git](https://github.com/your-username/cli-file-organizer.git)
    cd cli-file-organizer
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

### Basic Usage
Organize the current folder using the default config:
```bash
python organizer.py
