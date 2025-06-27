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
requirements_file = "requirements.txt"
if os.path.exists(requirements_file):
    print(f"Installing packages from {requirements_file}...")
    subprocess.run([python_path, "-m", "pip", "install", "-r", requirements_file], check=True)
else:
    print("No requirements.txt file found. Skipping package installation.")
