
from pathlib import Path
import json

def generate_mkdocs_yml(config_path="project_config.json", output_path="mkdocs.yml"):
    config_file = Path(config_path)
    if not config_file.exists():
        print(f"❌ Config file not found: {config_path}")
        return

    with open(config_file, "r", encoding="utf-8") as f:
        config = json.load(f)

    site_name = config.get("site_name", "index MD")
    site_description = config.get("description", "Professional documentation for your project using MkDocs")
    site_author = config.get("author", "Tamer")
    site_url = config.get("site_url", f"https://{config.get('author_username','username')}.github.io/{config.get('name','project')}/")
    repo_name = config.get("repo_name", f"{config.get('author_username','username')}/{config.get('name','project')}")
    repo_url = config.get("url", f"https://github.com/{repo_name}")

    mkdocs_yml = f"""site_name: {site_name}
site_description: {site_description}
site_author: {site_author}
site_url: {site_url}

repo_name: {repo_name}
repo_url: {repo_url}
edit_uri: edit/main/docs/

theme:
  name: material
  language: en
  custom_dir: docs/overrides
  logo: screenshots/logo.svg
  favicon: screenshots/favicon.ico
  features:
    - navigation.tabs
    - navigation.top
    - navigation.indexes
    - search.highlight
    - search.suggest
    - content.code.annotate
    - content.code.copy
    - toc.integrate
    - palette.toggle
  copyright: "© 2025 {site_author}. All rights reserved."
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: slate
      primary: teal
      accent: deep purple
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: teal
      accent: lime

nav:
  - Home: index.md
  - Sections:
      - About: sections/about.md
      - Contact: sections/contact.md
      - Important Links: sections/important-links.md
      - Privacy Policy: sections/privacy.md
      - Terms of Service: sections/terms.md
      - Code of Conduct: CODE_OF_CONDUCT.md

markdown_extensions:
  - admonition
  - codehilite
  - footnotes
  - meta
  - toc:
      permalink: true
  - tables
  - pymdownx.superfences
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.emoji
  - pymdownx.details
  - pymdownx.tasklist:
      custom_checkbox: true

plugins:
  - search
  - awesome-pages
  - git-revision-date
  - macros

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/{config.get("author_username","TamerOnLine")}
    - icon: fontawesome/brands/linkedin
      link: https://www.linkedin.com/in/{config.get("author_username","tameronline")}/
  version:
    provider: git

extra_css:
  - stylesheets/extra.css

extra_javascript:
  - javascripts/extra.js
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(mkdocs_yml.strip())

    print(f"✅ Generated {output_path} from {config_path}")

if __name__ == "__main__":
    generate_mkdocs_yml()
