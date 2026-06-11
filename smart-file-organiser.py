import os
import shutil
from datetime import datetime
# Get the base directory where all files are present initially
base_directory=r'E:\coding\PYTHON\All_files'
# Create mapping for file extensions and thier respective folder
extensions = {'.txt':'TEXT','.pdf':'PDF','.jpeg':'IMAGE','.py':'PYTHON','.pptx':'PPT','.docx':'WORD','.jpg':'IMAGE'}
# Create a list of all files present in base directory
list_of_files = os.listdir(base_directory)
#Create a log file for movement track
logfile = os.path.join(base_directory, 'log.txt')
with open(logfile, "a") as fh:
    for file in list_of_files:
        # Get the address of file
        source=os.path.join(base_directory,file)
        # Check if given address is of file, otherwise continue
        if not os.path.isfile(source):
            continue
        # Take the extension of the file
        extension = os.path.splitext(file)[-1].lower()
        # Now check file's extension and then get its destination folder and its path
        destination_folder = extensions.get(extension,'OTHER')
        destination_path = os.path.join(base_directory,destination_folder)
        # Check if destination folder exists,otherwise create it
        if not os.path.exists(destination_path):
            os.mkdir(destination_path)
        # For time info regardig the modification of file
        timestamp = os.path.getmtime(source)
        date = datetime.fromtimestamp(timestamp)
        year = str(date.year)
        month = date.strftime("%B")
        # Move file into its destination folder
        shutil.move(source,destination_path)
        # Add the record of all movements in log file
        fh.write(f"MOVED '{file}' --> {destination_folder} on {month}-{year}\n")