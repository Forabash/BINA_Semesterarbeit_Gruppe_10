# -*- coding: utf-8 -*-
"""
Created on Tue Apr 15 15:43:05 2025

@author: rapha
"""

import os
import shutil
from datetime import datetime

# Source and destination folders
source_folder = "C:\\Users\\rapha\\OST\\TS-BINA - Gruppenarbeit - General\\zArchiv\\99 CIA_Factbook\\weekly_json(1)\\weekly_json"
destination_folder = "C:\\Users\\rapha\\OST\\TS-BINA - Gruppenarbeit - General\\zArchiv\\99 CIA_Factbook\\weekly_json(1)\\weekly_output"

# Ensure the destination folder exists
os.makedirs(destination_folder, exist_ok=True)

# Dictionary to store the latest file per year
latest_files = {}

# Iterate through all JSON files in the source folder
for filename in os.listdir(source_folder):
    if filename.endswith(".json"):
        # Extract date from the filename (assuming format: data_YYYY-MM-DD.json)
        try:
            # Adjust this pattern to match your filenames
            date_str = filename.split('_')[0].replace('_.json', '')
            #print(filename)
            #print(date_str)
            file_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print(f"Skipping file with invalid date format: {filename}")
            continue

        # Update latest file for the year if necessary
        year = file_date.year
        if year not in latest_files or file_date > latest_files[year]['date']:
            latest_files[year] = {'filename': filename, 'date': file_date}

# Copy the latest files to the destination folder
for year, info in latest_files.items():
    src_path = os.path.join(source_folder, info['filename'])
    dest_path = os.path.join(destination_folder, info['filename'])
    shutil.copy(src_path, dest_path)
    print(f"Copied: {info['filename']} to {destination_folder}")

print("All latest files have been copied.")
