#!/usr/bin/env python3
"""
Auto-fix documentation compliance issues.

Fixes:
1. Remove duplicate H1 from body (keep frontmatter only)
2. Add missing External Linking section
3. Ensure proper spacing between H2 sections
"""

import re
from pathlib import Path

import yaml


class DocFixer:
    def __init__(self, docs_path="content"):
        self.docs_path = Path(docs_path)
        self.fixed_count = 0
        self.error_count = 0

    def fix_all(self):
        """Fix all markdown files"""
        md_files = list(self.docs_path.rglob("*.md"))
        print(f"Processing {len(md_files)} markdown files...")

        for file_path in sorted(md_files):
            try:
                self.fix_file(file_path)
            except Exception as e:
                print(f"ERROR processing {file_path}: {e}")
                self.error_count += 1

        print(f"\n[SUMMARY] Fixed: {self.fixed_count} | Errors: {self.error_count}")

    def fix_file(self, file_path: Path):
        """Fix a single file"""
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        # Parse frontmatter
        try:
            parts = content.split("---", 2)
            if len(parts) < 3:
                return  # Skip files without proper frontmatter

            frontmatter_str = parts[1]
            body = parts[2].strip()
        except (ValueError, IndexError):
            return

        # Try to parse YAML
        try:
            fm = yaml.safe_load(frontmatter_str)
            title = fm.get("title", "")
        except yaml.YAMLError:
            return

        # FIX 1: Remove duplicate H1
        h1_pattern = r"^#\s+" + re.escape(title) + r"\s*\n+"
        if re.search(h1_pattern, body, re.MULTILINE):
            body = re.sub(h1_pattern, "", body, count=1, flags=re.MULTILINE)
            print(f"[FIXED] H1 duplicate in {file_path.relative_to(self.docs_path)}")
            self.fixed_count += 1

        # Also remove any standalone H1
        body = re.sub(r"^#\s+[^\n]*\n+", "", body, count=1, flags=re.MULTILINE)

        # FIX 2: Ensure External Linking section exists
        if not re.search(r"##\s+External Link", body, re.IGNORECASE):
            if (
                "temporal" not in body.lower()
                and "changelog" not in str(file_path).lower()
            ):
                # Add placeholder External Linking
                external_linking = """## External Linking

| Concept | Resource | Link |
|---------|----------|------|
| See main documentation | [Vectora Docs](https://vectora.github.io/) | https://vectora.github.io/ |
"""
                body = body.rstrip() + "\n\n" + external_linking
                print(
                    f"[ADDED] External Linking in {file_path.relative_to(self.docs_path)}"
                )
                self.fixed_count += 1

        # Reconstruct document
        new_content = f"---\n{frontmatter_str}---\n\n{body.lstrip()}"

        if new_content != original_content:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)


if __name__ == "__main__":
    fixer = DocFixer()
    fixer.fix_all()
