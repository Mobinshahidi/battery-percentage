
# Battery Alert Service 🔋

The Battery Alert Service is a Python script that monitors the battery level of a Windows laptop and displays alert messages when certain conditions are met. The script is designed to run continuously in the background as a Windows service, providing real-time notifications to the user.


## Features 

- Monitors the battery level and power status (plugged in or unplugged).
- Displays alert messages when the battery reaches a specific percentage (e.g., 100%).
- Calculates and displays the estimated time remaining until the battery is fully charged or depleted.
- Runs as a Windows service, allowing for seamless background execution without user intervention.
- Built using the psutil library for battery monitoring and ctypes for displaying message dialogs.


## Prerequisites
- Python 3.x installed on the system.
- PyInstaller library for converting the Python script into an executable.
- NSSM (Non-Sucking Service Manager) for creating and managing Windows services.

## Installation

1. Clone or download the repository to your local machine.

2. Install the required Python packages using pip:

```bash
pip install psutil
```

3. Install PyInstaller for converting the script into an executable:

```bash
pip install pyinstaller
```
4. Download and extract NSSM from the official website: [NSSM - the Non-Sucking Service Manager](https://nssm.cc/download).

    
## Usage

1. Edit the `battery_alert.py` script to customize the battery percentage threshold and other parameters if needed.

2. Convert the Python script into an executable using PyInstaller:

```bash
pyinstaller --onefile battery_alert.py
```

3. Use NSSM to create a Windows service for the executable:
```bash
nssm install batteryAlert "C:\path\to\battery_alert.exe"
```

4. Start the batteryAlert service:

```bash
net start batteryAlert
```

## Troubleshooting
- If you encounter any issues with the service, check the Event Viewer or system logs for error messages.
- Ensure that the service has the necessary permissions and dependencies to run successfully.
- Verify that the NSSM executable directory is added to the system's PATH variable.
- Update NSSM to the latest version if you encounter compatibility issues.

## Contributing
Contributions to the project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.
## License

This project is licensed under the [MIT License](https://github.com/Mobinshahidi/battery-percentage/blob/main/docs/LICENSE).

