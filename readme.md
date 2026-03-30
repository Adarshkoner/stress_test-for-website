-----On Kali Linux------

# 1. Update system
sudo apt update && sudo apt upgrade -y

# 2. Install Python & pip if not already
sudo apt install python3 python3-pip -y

# 3. Navigate to project folder
cd stress-test/

# 4. Install dependencies
pip3 install -r requirements.txt


-------On Windows Terminal-----

# 1. Ensure Python is installed (check with python --version)
# If not, install from https://www.python.org/downloads/

# 2. Navigate to project folder
cd stress-test

# 3. Install dependencies
pip install -r requirements.txt


-------▶️ Running the Script------

command:--  python stress_test.py https://yourwebsite.com --check https://yourwebsite.com/ -s 100 -p 200 -m 2000 -r 50 -d 5m

command:--  --check     → any stable page (homepage, about, etc.)

command:--  -s          → starting users

command:--  -p          → step increase

command:--  -m          → maximum users

command:--  -r          → spawn rate

command:--  -d          → duration per step