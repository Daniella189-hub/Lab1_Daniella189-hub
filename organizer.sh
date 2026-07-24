#!/bin/bash
# organizer.sh
# Automates archiving of grades.csv, resets the workspace, and logs the action.

 
# adding the content of the grades.csv file 
dir_arch="archive"
log_file="organizer.log"
source_file="grades.csv"

#1.directory archive
if [ ! -d "$dir_arch" ]; then
    mkdir "$dir_arch"
    echo "Created archive directory: $dir_arch"
fi

#2. Timestamp Generation
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")

# 3. The Archival Process
if [ -f "$source_file" ]; then

    BASE_NAME="${source_file%.csv}" 
    NEW_NAME="${BASE_NAME}_${TIMESTAMP}.csv" 

    # Move (rename) the original file into the archive directory
    mv "$source_file" "$dir_arch/$NEW_NAME"

#4. Workspace Reset
    touch "$source_file"

#5. Logging
    echo "[$TIMESTAMP] Original: $source_file -> Archived: $dir_arch/$NEW_NAME" >> "$log_file"

    echo "Success: $source_file archived as $dir_arch/$NEW_NAME"
    echo "A new empty $source_file has been created for the next batch."
else
    echo "Error: $source_file not found in the current directory. Nothing to archive."
    echo "[$TIMESTAMP] ERROR: $source_file not found. No archival performed." >> "$log_file"
    exit 1
fi
