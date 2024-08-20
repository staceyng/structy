#!/bin/bash

# Check if a file name is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <file_name> [output_directory]"
  exit 1
fi

# Set the file name and outpur variable
FILE_NAME=$1
OUTPUT_DIR=${2:-.}

# Create the Python file
cat <<EOL > "${OUTPUT_DIR}/${FILE_NAME}.py"
from node import Node

def ${FILE_NAME}(root):
    pass

if __name__ == "__main__":
    pass

EOL

echo "File '${OUTPUT_DIR}/${FILE_NAME}.py' created successfully."

