#!/bin/bash

VENV_DIR="/src/venv"
SCRIPT="/src/main.py"


if [ ! -d "$VENV_DIR" ]; then
  echo "the virtual environment not exist. creating venv..."
  /usr/local/bin/python -m venv "$VENV_DIR"

  "$VENV_DIR/bin/pip" install -r /src/requirements.txt

  if [ $? -ne 0 ]; then
    echo "Error downloading packages."
    exit 1
  fi
fi

source "$VENV_DIR/bin/activate"

if [ ! -f "$SCRIPT" ]; then
  echo "The file $SCRIPT not found."
  exit 1
fi

"$VENV_DIR/bin/python" "$SCRIPT"
