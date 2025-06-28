import json
from pathlib import Path

def generate_setup_py(config):
    setup_code = f"""from setuptools import setup, find_packages

setup(
    name="{config.get('name', 'unknown')}",
    version="{config.get('version', '0.1.0')}",
    description="{config.get('description', '')}",
    author="{config.get('author', '')}",
    author_email="{config.get('author_email', '')}",
    url="{config.get('url', '')}",
    packages=find_packages(include=["{config.get('name', '').replace('-', '_')}", "{config.get('name', '').replace('-', '_')}.*"]),
    include_package_data=True,
    package_data={{"{config.get('name', '').replace('-', '_')}": {config.get('include_patterns', [])} }},
    install_requires={config.get('install_requires', [])},
    entry_points={{
        'console_scripts': {config.get('console_scripts', [])}
    }},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires="{config.get('python_version', '>=3.8')}",
)
"""
    with open("setup.py", "w", encoding="utf-8") as f:
        f.write(setup_code.strip())
    print("✅ Generated setup.py")


def generate_pyproject_toml(config):
    # إعداد dependencies بشكل آمن
    dependencies_list = config.get("install_requires", [])
    dependencies = ",\n".join([f'    "{pkg}"' for pkg in dependencies_list])

    # إعداد console_scripts بشكل آمن
    console_scripts_raw = config.get("console_scripts", [])
    console_scripts = "\n".join([
        f'{cmd.partition("=")[0].strip()} = "{cmd.partition("=")[2].strip()}"'
        for cmd in console_scripts_raw if "=" in cmd
    ])

    toml_content = f"""[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{config.get('name', 'unknown')}"
version = "{config.get('version', '0.1.0')}"
description = "{config.get('description', '')}"
authors = [{{ name="{config.get('author', '')}", email="{config.get('author_email', '')}" }}]
requires-python = "{config.get('python_version', '>=3.8')}"
dependencies = [
{dependencies}
]

[project.scripts]
{console_scripts}
"""
    with open("pyproject.toml", "w", encoding="utf-8") as f:
        f.write(toml_content.strip())
    print("✅ Generated pyproject.toml")


def main():
    config_path = "project_config.json"
    if not Path(config_path).exists():
        print("❌ project_config.json not found.")
        return

    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)

    current_version = config.get("version", "0.1.0")
    new_version = input(f"📌 Enter version [{current_version}]: ").strip()
    if not new_version:
        new_version = current_version
    config["version"] = new_version

    # إعادة كتابة project_config.json بعد تحديث النسخة
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

    generate_setup_py(config)
    generate_pyproject_toml(config)


if __name__ == "__main__":
    main()
