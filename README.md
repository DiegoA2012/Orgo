
# Orgo: The Automatic File Organizer

## Introduction
Welcome to Orgo, the Automatic File Organizer! This script helps you keep your Downloads folder organized by automatically moving files into folders based on their types.

## Features
- Simple GUI to start and stop the file organizing process.
- Option to choose between different time intervals for automatic organization.
- Supports various file types including text, documents, images, audio, and more.

## How to Use
1. Run the script. A GUI window will appear.
2. Choose a time interval for automatic organization: 30 seconds, 1 minute, or 5 minutes.
3. Click the "Start" button to begin the organization process.
4. Click the "Stop" button to stop the organization process.

## Dependencies
- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## How it Works
The script uses Python's os and shutil libraries to move files from the Downloads folder to their respective folders. The Tkinter library is used for the GUI. The script also runs the organizing function in a separate thread, allowing the GUI to remain responsive.

