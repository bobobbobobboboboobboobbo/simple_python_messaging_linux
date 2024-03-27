import random
import time
import sys
import os

# Define a function to play an mp3 file using the command line
def play_mp3(file_path):
    # Use the system's default command to play the mp3 file
    os.system(f"start {file_path}")

# Call the function to play "song.mp3"
play_mp3('/home/codespace/codespaces-electrictboggaloo/Untitled song(4).mp3')

# Print a success message
print("Playing song.mp3")
