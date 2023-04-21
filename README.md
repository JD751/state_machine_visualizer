State Machine Visualization

This project implements a simple client to query and visualize the structure of a state machine hosted on an MEQ server. The state machine consists of 26 states named from A to Z, where A is always the initial state and Z is always the terminal state. Each state, except Z, has exactly 3 transitions, described by actions "1", "2", and "3".

Installation
Before running this project, make sure you have Python 3.7 or later installed on your system. Additionally, you need to install Graphviz to visualize the state machine. Follow the Graphviz installation instructions for your operating system.

For macOS users, you can use Homebrew:
brew install graphviz

After installing Graphviz, add its executables to your system's PATH. Refer to the instructions in this previous response.

Creating a virtual environment (optional)
It's recommended to create a virtual environment to isolate the project's dependencies. To create a virtual environment, run the following commands:

python3 -m venv env

source env/bin/activate  # For Windows, use `env\Scripts\activate`

Installing dependencies
Install the required Python dependencies by running:

pip install -r requirements.txt

Usage
To build the state machine structure, run:

python state_machine.py

This script will create a dictionary containing the state machine structure.

To visualize the state machine, run:

python visualize.py

This script will generate an image file named state_machine.png with the state machine visualization.

License
This project is licensed under the MIT License. See the LICENSE file for details.