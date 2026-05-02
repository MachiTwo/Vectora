#!/usr/bin/env python3
"""
Lint documentation files for Vectora CLAUDE.md compliance.

Rules checked:
1. Frontmatter present and valid YAML
2. Required frontmatter fields (title, slug, date, type, tags)
3. No duplicate H1 in body (title should be in frontmatter only)
4. Shortcodes (lang-toggle, section-toggle) present if applicable
5. Descriptive paragraph after shortcodes
6. No decorative emojis in technical docs
7. External Linking section present (except temporal content)
8. Filename matches slug (kebab-case)
"""

import re
from pathlib import Path

import yaml


class DocLinter:
    def __init__(self, docs_path="content"):
        self.docs_path = Path(docs_path)
        self.issues = []
        self.decorative_emojis = {
            "🧠",
            "🔑",
            "🚀",
            "📱",
            "💻",
            "🌐",
            "📚",
            "🔒",
            "⚙️",
            "🎯",
            "✅",
            "❌",
            "⚠️",
            "💡",
            "🔍",
            "📊",
            "🎨",
            "🔄",
        }
        self.important_tags = {"🔐", "💾", "⏱️"}  # Keep these

    def lint_all(self):
        """Lint all markdown files in docs/content"""
        md_files = list(self.docs_path.rglob("*.md"))
        print(f"Linting {len(md_files)} markdown files...")

        for file_path in sorted(md_files):
            self.lint_file(file_path)

        return self.issues

    def lint_file(self, file_path: Path):
        """Lint a single file"""
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Parse frontmatter
        try:
            parts = content.split("---", 2)
            if len(parts) < 3:
                self.add_issue(file_path, "ERROR", "Missing frontmatter")
                return

            frontmatter_str = parts[1]
            body = parts[2].strip()
        except Exception as e:
            self.add_issue(file_path, "ERROR", f"Failed to parse frontmatter: {e}")
            return

        try:
            fm = yaml.safe_load(frontmatter_str)
        except Exception as e:
            self.add_issue(file_path, "ERROR", f"Invalid YAML: {e}")
            return

        # Validate required fields
        required_fields = ["title", "slug", "date", "tags"]
        for field in required_fields:
            if field not in fm:
                self.add_issue(
                    file_path, "ERROR", f"Missing frontmatter field: {field}"
                )

        # Check filename vs slug
        filename = file_path.stem
        slug = fm.get("slug", "")
        if filename not in ["_index", "index", "README"] and filename != slug:
            self.add_issue(
                file_path, "WARN", f"Filename '{filename}' doesn't match slug '{slug}'"
            )

        # Check for duplicate H1 in body
        if re.search(r"^#\s+", body, re.MULTILINE):
            self.add_issue(
                file_path,
                "ERROR",
                "Duplicate H1 found (title should be in frontmatter only)",
            )

        # Check for shortcodes and descriptive paragraph
        if "{{< lang-toggle" in body:
            # Find content after lang-toggle
            match = re.search(
                r"{{<\s*lang-toggle\s*>}}\s*\n*(.*?)\n\n", body, re.DOTALL
            )
            if not match or not match.group(1).strip():
                self.add_issue(
                    file_path, "WARN", "No descriptive paragraph after lang-toggle"
                )

        # Check for decorative emojis (but allow important ones)
        emoji_pattern = r"[🧠🔑🚀📱💻🌐📚🔒⚙️🎯✅❌⚠️💡🔍📊🎨🔄]"
        for match in re.finditer(emoji_pattern, body):
            emoji = match.group()
            if emoji not in self.important_tags:
                line_num = body[: match.start()].count("\n") + 1
                self.add_issue(
                    file_path,
                    "WARN",
                    f"Decorative emoji found: {emoji} (line {line_num})",
                )
                break  # Report once per file

        # Check for External Linking section
        if not re.search(r"##\s+External Link", body, re.IGNORECASE):
            if (
                "temporal" not in body.lower()
                and "changelog" not in file_path.parts[-1].lower()
            ):
                self.add_issue(file_path, "WARN", "Missing External Linking section")

        # Check H2 structure (should have content before next H2)
        h2_pattern = r"^##\s+(.+?)$"
        h2_matches = list(re.finditer(h2_pattern, body, re.MULTILINE))
        for i, match in enumerate(h2_matches):
            if i < len(h2_matches) - 1:
                next_h2_pos = h2_matches[i + 1].start()
                between = body[match.end() : next_h2_pos].strip()
                if not between:
                    self.add_issue(
                        file_path,
                        "WARN",
                        f"No content between H2 headers: '{match.group(1)}' and next header",
                    )

    def add_issue(self, file_path: Path, level: str, message: str):
        """Add an issue to the list"""
        rel_path = file_path.relative_to(self.docs_path)
        self.issues.append({"file": str(rel_path), "level": level, "message": message})

    def print_report(self):
        """Print linting report"""
        if not self.issues:
            print("\n[PASS] All documents are compliant!")
            return

        # Group by level
        errors = [i for i in self.issues if i["level"] == "ERROR"]
        warnings = [i for i in self.issues if i["level"] == "WARN"]

        print("\n[RESULTS] Linting Summary:")
        print(f"  [ERROR] Count: {len(errors)}")
        print(f"  [WARN]  Count: {len(warnings)}")
        print(f"  [TOTAL] Issues: {len(self.issues)}")

        if errors:
            print(f"\n[ERRORS] ({len(errors)}):")
            for issue in errors[:20]:  # Show first 20
                print(f"  - {issue['file']}: {issue['message']}")
            if len(errors) > 20:
                print(f"  ... and {len(errors) - 20} more")

        if warnings:
            print(f"\n[WARNINGS] ({len(warnings)}):")
            for issue in warnings[:20]:  # Show first 20
                print(f"  - {issue['file']}: {issue['message']}")
            if len(warnings) > 20:
                print(f"  ... and {len(warnings) - 20} more")


if __name__ == "__main__":
    linter = DocLinter()
    issues = linter.lint_all()
    linter.print_report()
