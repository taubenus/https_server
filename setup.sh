#!/bin/bash

openssl req -newkey rsa:4096 -nodes -keyout key.pem -x509 -days 365 -out cert.pem
echo "SSL certificate and key generated."

# Get the script directory (adjust path if needed)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
HTTPS_SCRIPT="$SCRIPT_DIR/https_server.py"

# Define the alias
ALIAS_CMD="alias https='python \"$HTTPS_SCRIPT\"'"

# Add alias to ~/.bashrc if not already present
if ! grep -Fxq "$ALIAS_CMD" ~/.bashrc; then
    echo "$ALIAS_CMD" >> ~/.bashrc
    echo "Alias 'https' added to ~/.bashrc. Run 'source ~/.bashrc' to activate."
else
    echo "Alias already exists in ~/.bashrc."
fi

