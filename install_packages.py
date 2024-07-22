import subprocess
import sys

def install_requirements():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

# Contoh penggunaan
if __name__ == "__main__":
    install_requirements()
