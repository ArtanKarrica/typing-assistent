#!/bin/bash

# Create a Python virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Run the application
echo "Starting the application..."
python main.py

# Deactivate the virtual environment after the script finishes
deactivate
echo "Application has stopped. Virtual environment deactivated."
