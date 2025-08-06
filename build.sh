#!/bin/bash
set -e
python -m pip install --quiet pyinstaller PySide6
pyinstaller --noconfirm --onefile gui/main.py --name btctools_gui
