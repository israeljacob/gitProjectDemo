# Keylogger Project

## Project Description
This project is a secure keylogging and monitoring system designed for ethical research and security auditing. It provides a mechanism to capture and analyze keystrokes while ensuring data integrity through encryption. The system allows storing logs locally or securely transmitting them over a network. Additionally, it includes a web-based dashboard for visualizing captured data and managing monitored machines.

## Project Structure
```
Keylogger_project/
├── logger/
│   ├── keylogger/                    # Files responsible for capturing keystrokes
│   │   ├── inter_face.py             # Interface for keylogger implementation
│   │   ├── keylogger_service.py      # Keylogger service logic
│   │   ├── KeyLoggerManager.py       # Manages keylogging operations
│   │   ├── special_characters.py     # Defines special character mappings
│   ├── writer/                        # Files for storing captured data
│   │   ├── FileWriter.py             # Handles local file writing
│   │   ├── IWriter.py                # Interface for different writing methods
│   │   ├── NetWorkWriter.py          # Handles sending logs over the network
├── server/                            # Flask-based API for data management
│   ├── data/                          # Encrypted logs and configuration files
│   ├── utilities/
│   │   ├── config.py                  # Application configuration settings
│   │   ├── encryption_utils.py        # Encryption utility functions
│   │   ├── file_utils.py              # File handling utilities
│   │   ├── help_utils.py              # Helper functions for data processing
│   ├── app.py                         # Server execution file
├── user/                              # Web-based user interface
│   ├── app.py                         # User interface execution file
│   ├── login.css                      # Stylesheet for login page
│   ├── login.html                     # Login page
│   ├── login.js                       # Login logic
│   ├── MachineData.css                # Stylesheet for machine data page
│   ├── MachineData.html               # Machine data visualization
│   ├── MachineData.js                 # Machine data processing logic
│   ├── MachinesManager.css            # Stylesheet for machine list management
│   ├── MachinesManager.html           # Machines list management dashboard
│   ├── MachinesManager.js             # Logic for managing machine list
│   ├── usernames_and_passwords.json   # Stores user credentials
├── utilities/
│   ├── encryptionDecryption/
│   │   ├── encryption.py              # XOR-based encryption implementation
│   │   ├── decryption.py              # XOR-based decryption implementation
│   ├── key.txt                         # Encryption key storage
├── setup.py                            # Script to check and create required files and directories
```

## Installation

### Prerequisites
Ensure that the following are installed on your system:
- Python 3.8 or later
- pip (Python package manager)
- Dependencies listed in `requirements.txt`

### Setting Up the Environment
Before running the system, execute the `setup.py` script, which will verify and create necessary files and directories if they do not exist:
```sh
python setup.py
```
Additionally, set up the following files:
1. **full_names.txt** – Add full names to this file, with each name on a new line.
2. **key.txt** – Insert a single-character encryption key in this file.
3. **usernames_and_passwords.json** – Populate this JSON file with username-password pairs in the following format:
```json
{
  "username1": "password1",
  "username2": "password2"
}
```

### Installing Required Packages
To install the necessary dependencies, run the following command:
```sh
pip install -r requirements.txt
```

## Running the Project

### Starting the Flask Server
To start the server, execute:
```sh
python server/app.py
```
The server will be available at `http://127.0.0.1:5000`

### Running the User-Side Service
The **user/app.py** script must be running at all times on the user's machine. It provides the necessary authentication and encryption key information to the frontend JavaScript files:
```sh
python user/app.py
```
Even if the main server runs on another machine, the user-side service must always be executed locally.

### Running the Keylogger
To start the keylogger, execute:
```sh
python logger/keylogger/KeyLoggerManager.py
```
## Features
- **Keystroke Logging**: Captures all keystrokes in real-time.
- **Encryption & Decryption**: Ensures secure data storage.
- **Local & Network Storage**: Logs can be stored locally or transmitted over a network.
- **Machine Monitoring**: Supports monitoring multiple machines with encrypted communication.
- **Web Dashboard**: Provides a user interface to view recorded data.
- **Authentication System**: Manages user access securely.
- **Configurable Storage**: Allows flexible storage options based on security needs.

## Security and Legal Disclaimer
This project is intended for educational and ethical research purposes only. Unauthorized use of keyloggers is illegal and may lead to legal consequences. Use this software responsibly and in compliance with applicable laws.

## Future Enhancements
- Strengthen encryption by implementing a more advanced algorithm.
- Add user authentication system.
- Develop a graphical interface for log management.
- Integrate real-time log visualization via the web interface.

## Contact
For further inquiries, reach out via [GitHub](https://github.com/israeljacob/keylogger_project).
