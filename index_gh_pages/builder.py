import os
import re
import subprocess
from pathlib import Path

LICENSE_LINK = "https://github.com/TamerOnLine/indexMD/blob/main/LICENSE"
DOCS_DIR = Path("docs")

def setup_docs_structure():
    folders = [
        "docs",
        "docs/sections",
        "docs/screenshots",
        "docs/stylesheets",
        "docs/overrides",
        "docs/overrides/partials"
    ]

    files = {
        "docs/index.md": "# Welcome to indexMD Documentation\n",
        "docs/sections/about.md": "## About\nThis section describes the project.",
        "docs/sections/contact.md": "## Contact\nYour contact details here.",
        "docs/sections/important-links.md": "## Important Links\nUseful resources go here.",
        "docs/sections/privacy.md": "## Privacy Policy\nYour privacy matters.",
        "docs/sections/terms.md": "## Terms and Conditions\nUsage terms go here.",
        "docs/stylesheets/extra.css": "/* Custom styles go here */",
        "docs/overrides/partials/footer.html": (
            "<footer>\n  <p>© 2025 Tamer Online</p>\n</footer>\n"
        )
    }

    for folder in folders:
        os.makedirs(folder, exist_ok=True)

    for path, content in files.items():
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

def clean_content(content: str) -> str:
    content = re.sub(r".*?\[Live Documentation\]\([^)]+\)\s*\n?", "", content)
    content = re.sub(r"\[.*?Back to Top.*?\]\([^)]+\)\s*\n?", "", content, flags=re.IGNORECASE)
    content = re.sub(r"## Table of Contents[\s\S]+?(?=\n## )", "", content)
    return content

def fix_links(content: str) -> str:
    content = content.replace("screenshots/", "screenshots/")
    content = content.replace("(../LICENSE)", f"({LICENSE_LINK})")
    content = content.replace("(LICENSE)", f"({LICENSE_LINK})")
    return content

def prepare_readme(readme_path="README.md", output_path="docs/index.md"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    content = clean_content(content)
    content = fix_links(content)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

def build_docs():
    subprocess.run(["mkdocs", "build"], check=True)
