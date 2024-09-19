import subprocess
import sys

subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "opencv-python"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "pycryptodome"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])

#bla bla bla
