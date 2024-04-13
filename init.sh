#!/bin/bash

# Install the required packages from requirements.txt

pip install -r requirements.txt
#!/bin/bash
clear
# Prompt the user for input
read -p "Enter (1) for server or (2) for client: " user_input

# Check if the input is valid
if [[ $user_input -eq 1 ]]; then
  # Run the server code
  python3 server.py
elif [[ $user_input -eq 2 ]]; then
  # Run the client code
  python3 client.py
else
  echo "Invalid input. Please enter 1 or 2."
fi
