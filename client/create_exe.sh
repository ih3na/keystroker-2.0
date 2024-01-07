#!/bin/bash

# Activate virtual environment (if applicable)
source bin/activate

# Install PyInstaller if not already installed
python -m pip install -r requirements.txt

# Create the executable
pyinstaller --onefile main.py --name keystroker

# Optionally, create a single-folder distribution
# pyinstaller --onedir main.py

# Executable will be in the "dist" directory
echo "Executable created in the dist directory!"
