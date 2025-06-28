import subprocess
import os
import shutil

desired_version = "3.12"
env_dir = "venv"

# 🧹 Remove existing environment if it exists
if os.path.exists(env_dir):
    print(f"Removing existing virtual environment: {env_dir}")
    shutil.rmtree(env_dir)

# 🆕 Create a new virtual environment with the desired Python version
print(f"Creating virtual environment with Python {desired_version}: {env_dir}")
subprocess.run(["py", f"-{desired_version}", "-m", "venv", env_dir], check=True)

# 🔍 Define paths
if os.name == "nt":
    pip_path = os.path.join(env_dir, "Scripts", "pip.exe")
    python_path = os.path.join(env_dir, "Scripts", "python.exe")
else:
    pip_path = os.path.join(env_dir, "bin", "pip")
    python_path = os.path.join(env_dir, "bin", "python")

# ⬆️ Upgrade pip
print("Upgrading pip...")
subprocess.run([python_path, "-m", "pip", "install", "--upgrade", "pip"], check=True)

# 📦 Install packages from requirements.txt if it exists
def install_requirements(file_name):
    if os.path.exists(file_name):
        print(f"📦 Installing packages from {file_name}...")
        subprocess.run([python_path, "-m", "pip", "install", "-r", file_name], check=True)
    else:
        print(f"⚠️ No {file_name} file found. Skipping.")

install_requirements("requirements.txt")
install_requirements("dev-requirements.txt")

