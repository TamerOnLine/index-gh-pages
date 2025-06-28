import json
import os
import glob

def read_requirements():
    if not os.path.exists("requirements.txt"):
        return []
    with open("requirements.txt") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def detect_console_scripts():
    scripts = []
    cli_path = os.path.join("index_gh_pages", "cli.py")
    if os.path.exists(cli_path):
        scripts.append("indexgh = index_gh_pages.cli:main")
    return scripts

def detect_files():
    files = []
    for name in ["README.md", "LICENSE"]:
        if os.path.exists(name):
            files.append(name)
    return files

def detect_patterns():
    patterns = []
    if glob.glob("index_gh_pages/*.yml"):
        patterns.append("index_gh_pages/*.yml")
    if glob.glob("index_gh_pages/*.cfg"):
        patterns.append("index_gh_pages/*.cfg")
    if os.path.exists("screenshots"):
        patterns.append("screenshots/*.gif")
    return patterns

def generate_config():
    with open("project_config_template.json") as f:
        config = json.load(f)

    config["install_requires"] = read_requirements()
    config["console_scripts"] = detect_console_scripts()
    config["include_files"] = detect_files()
    config["include_patterns"] = detect_patterns()

    with open("project_config.json", "w") as f:
        json.dump(config, f, indent=4)
    print("✅ Generated project_config.json")

if __name__ == "__main__":
    generate_config()
