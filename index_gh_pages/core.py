def convert_readme_to_index(readme_path="README.md", output_path="docs/index.md"):
    """تحويل README.md إلى index.md داخل docs/"""
    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
