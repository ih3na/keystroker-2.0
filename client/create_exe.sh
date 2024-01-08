#!/bin/bash

outfilename="keystroker"

# Check Options
while getops ":o:" opt; do
    case $opt in
        o)
            outfilename=$OPTARG
            ;;
        \?)
            echo "Invalid option: -$OPTARG" >&2
            exit 1
            ;;
        :)
            echo "Option -$OPTARG requires an argument." >&2
            exit 1
            ;;
    esac
done

# Activate virtual environment (if applicable)
source bin/activate

# Install PyInstaller if not already installed
python -m pip install -r requirements.txt

# Create the executable
pyinstaller --onefile main.py --name $outfilename

# Optionally, create a single-folder distribution
# pyinstaller --onedir main.py

# Executable will be in the "dist" directory
echo "Executable created in the dist directory!"
