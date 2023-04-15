# Refresh Rate Toggler

Refresh Rate Toggler is a simple Python app for Windows that allows you to toggle between 144Hz and 60Hz refresh rates directly from the system tray.

## Installation

To install Refresh Rate Toggler, follow these steps:

1. Clone or download the source code from the GitHub repository.
2. Install the required dependencies using pip: `pip install -r requirements.txt`
3. Run the app by executing the `main.py` script: `python main.py`

Alternatively, you can use PyInstaller to create a standalone executable:

1. Install PyInstaller: `pip install pyinstaller`
2. Build the executable: `pyinstaller --onefile --windowed main.py`
3. The executable will be located in the `dist` folder.

## Usage

Once the app is running, you can toggle between 144Hz and 60Hz refresh rates by clicking the "Toggle Refresh Rate" menu option in the system tray. The current refresh rate is displayed on the system tray icon.

To exit the app, click the "Exit" menu option in the system tray.

## License

Refresh Rate Toggler is licensed under the MIT License. See `LICENSE` for more information.
