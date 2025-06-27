import os
import re
from pathlib import Path

SOURCE_DIR = Path(".")
DOCS_DIR = Path("docs")

# Files to exclude from processing
EXCLUDE_FILES = {"mkdocs.yml"}

LICENSE_LINK = "https://github.com/TamerOnLine/indexMD/blob/main/LICENSE"

def clean_content(content: str) -> str:
    """Remove specific sections and links from the markdown content.

    Args:
        content (str): Original markdown content.

    Returns:
        str: Cleaned markdown content with unwanted sections removed.
    """
    content = re.sub(r".*?\[Live Documentation\]\([^)]+\)\s*\n?", "", content)
    content = re.sub(r"\[.*?Back to Top.*?\]\([^)]+\)\s*\n?", "", content, flags=re.IGNORECASE)
    content = re.sub(r"## Table of Contents[\s\S]+?(?=\n## )", "", content)
    return content

def fix_links(content: str) -> str:
    """Update or fix specific links within the markdown content.

    Args:
        content (str): Markdown content with links.

    Returns:
        str: Markdown content with updated links.
    """
    content = content.replace("screenshots/", "screenshots/")
    content = content.replace("(../LICENSE)", f"({LICENSE_LINK})")
    content = content.replace("(LICENSE)", f"({LICENSE_LINK})")
    return content

def write_to_docs(filename: str, content: str):
    """Write processed content to the appropriate file in the docs directory.

    Args:
        filename (str): Name of the markdown file.
        content (str): Processed markdown content to write.
    """
    output_path = DOCS_DIR / "index.md" if filename == "README.md" else DOCS_DIR / filename

    os.makedirs(output_path.parent, exist_ok=True)

    lines = content.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    content = '\n'.join(lines)

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Written: {output_path}")

def process_markdown_files():
    """Process all markdown files in the source directory excluding specified files.

    Cleans and updates links in each file before saving them to the docs directory.
    """
    md_files = [f for f in SOURCE_DIR.glob("*.md") if f.name not in EXCLUDE_FILES]

    for md_file in md_files:
        print(f"Processing {md_file.name}...")
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        cleaned = clean_content(content)
        fixed = fix_links(cleaned)

        write_to_docs(md_file.name, fixed)

    print("\nAll markdown files have been processed into the docs/ folder.\n")

if __name__ == "__main__":
    process_markdown_files()
