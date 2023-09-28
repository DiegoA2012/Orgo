
# Import necessary modules from the Tkinter library for GUI
from tkinter import Tk, Label, Button, Radiobutton, IntVar
# Import os and shutil for file operations, time for time.sleep, and threading for running organize_files in a separate thread
import os
import shutil
import time
import threading

# Define the main class for the Tkinter app
class OrgoApp:
    def __init__(self, master):
        self.master = master  # Main window for Tkinter
        self.stop_flag = False  # Initialize flag to control stopping the organizer
        master.title("Orgo: The Automatic File Organizer")  # Set the title of the window

        # Create and pack a label prompting the user to choose a time interval
        self.label = Label(master, text="Choose the time interval for automatic organization:")
        self.label.pack()

        # Initialize a Tkinter variable to hold the interval choice and create radio buttons for each choice
        self.interval_choice = IntVar()
        self.radio_30s = Radiobutton(master, text="30 seconds", variable=self.interval_choice, value=30)
        self.radio_1m = Radiobutton(master, text="1 minute", variable=self.interval_choice, value=60)
        self.radio_5m = Radiobutton(master, text="5 minutes", variable=self.interval_choice, value=300)
        
        # Pack the radio buttons into the Tkinter window
        self.radio_30s.pack()
        self.radio_1m.pack()
        self.radio_5m.pack()

        # Create and pack a "Start" button that calls the start_organizing method when clicked
        self.start_button = Button(master, text="Start", command=self.start_organizing)
        self.start_button.pack()

        # Create and pack a "Stop" button that calls the stop_organizing method when clicked
        self.stop_button = Button(master, text="Stop", command=self.stop_organizing)
        self.stop_button.pack()

    # Method to start the file organizing process
    def start_organizing(self):
        self.stop_flag = False  # Reset the stop flag when starting
        interval = self.interval_choice.get()  # Get the chosen interval from the radio buttons
        print(f"Starting to organize files every {interval} seconds.")
        
        # Run the organize_files function in a separate thread so that the GUI remains responsive
        thread = threading.Thread(target=self.run_organizer, args=(interval,))
        thread.start()

    # Method to stop the file organizing process
    def stop_organizing(self):
        self.stop_flag = True  # Set the stop flag to stop the while loop in run_organizer
        print("Stopping the file organization.")

    # Method that runs the organize_files function in a loop with a sleep interval
    def run_organizer(self, interval):
        while not self.stop_flag:  # Keep running until the stop flag is set
            organize_files()  # Call the main file organizing function
            time.sleep(interval)  # Wait for the specified interval before the next iteration

# Main function to organize files
def organize_files():
    source_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    file_list = os.listdir(source_folder)
    file_type_mapping = { # Image Files
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'gif': 'Images',
    'bmp': 'Images',
    'svg': 'Images',
    'tiff': 'Images',
    
    # Audio Files
    'mp3': 'Audio',
    'wav': 'Audio',
    'ogg': 'Audio',
    'flac': 'Audio',
    'aac': 'Audio',
    
    # Video Files
    'mp4': 'Video',
    'avi': 'Video',
    'mkv': 'Video',
    'flv': 'Video',
    'mov': 'Video',
    
    # Compressed Files
    'zip': 'Compressed',
    'rar': 'Compressed',
    'tar': 'Compressed',
    'gz': 'Compressed',
    'bz2': 'Compressed',
    
    # Code Files
    'py': 'Code',
    'js': 'Code',
    'html': 'Code',
    'css': 'Code',
    'java': 'Code',
    'c': 'Code',
    'cpp': 'Code',
    
    # Spreadsheet and Presentations
    'xls': 'Spreadsheets',
    'xlsx': 'Spreadsheets',
    'csv': 'Spreadsheets',
    'ppt': 'Presentations',
    'pptx': 'Presentations',
    
    # Database Files
    'sql': 'Databases',
    'db': 'Databases', }  

    for file_name in file_list:
        file_path = os.path.join(source_folder, file_name)
        
        # Skip if it's a directory
        if not os.path.isfile(file_path):
            continue

        file_extension = file_name.split('.')[-1]
        dest_folder = file_type_mapping.get(file_extension, 'Others')
        dest_path = os.path.join(source_folder, dest_folder)

        if not os.path.exists(dest_path):
            os.makedirs(dest_path)

        shutil.move(file_path, os.path.join(dest_path, file_name))

# Initialize Tkinter and run the app
root = Tk()
app = OrgoApp(root)
root.mainloop()
