import os

import yaml

# Configurações de Diretórios
CONTENT_DIR = "docs/content"
INDEX_FILE = os.path.join(CONTENT_DIR, "_index.md")
INDEX_FILE_EN = os.path.join(CONTENT_DIR, "_index.en.md")


def parse_doc(path, lang="pt"):
    """Parse documentation file and extract metadata."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.startswith("---"):
            return None

        parts = content.split("---")
        if len(parts) < 3:
            return None

        front = yaml.safe_load(parts[1])
        if not (front and front.get("title")):
            return None

        # URL Generation
        base_path = os.path.dirname(path)
        dir_url = base_path.replace(CONTENT_DIR, "").replace("\\", "/").strip("/")

        # Override slug if present in frontmatter
        if front.get("slug"):
            parts_url = dir_url.split("/")
            parts_url[-1] = str(front["slug"])
            dir_url = "/".join(parts_url)

        url = f"/{dir_url}/"
        if lang == "en":
            url = f"/en{url}"

        return {
            "title": front["title"],
            "url": url,
            "lang": lang,
        }
    except Exception as e:
        print(f"Error processing {path}: {e}")
        return None


def escape_markdown(text):
    """Escape markdown special characters."""
    return str(text).replace("[", "\\[").replace("]", "\\]")


def write_if_changed(target, content):
    """Write content only if it changed."""
    content = content.rstrip() + "\n"
    if os.path.exists(target):
        with open(target, "r", encoding="utf-8") as f:
            if f.read() == content:
                return False

    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return True


def main():
    """Generate documentation index from content structure."""
    docs_pt = []
    docs_en = []

    # Scan for documentation files
    for root, _, files in os.walk(CONTENT_DIR):
        for file in files:
            if file == "index.md":
                doc = parse_doc(os.path.join(root, file), lang="pt")
                if doc:
                    docs_pt.append(doc)
            elif file == "index.en.md":
                doc = parse_doc(os.path.join(root, file), lang="en")
                if doc:
                    docs_en.append(doc)

    # Sort alphabetically by title
    docs_pt.sort(key=lambda d: d["title"])
    docs_en.sort(key=lambda d: d["title"])

    # Generate PT Index
    idx_content = "---\n"
    idx_content += "title: Vectora Documentation\n"
    idx_content += "---\n\n"
    idx_content += "{{< lang-toggle >}}\n\n"

    if docs_pt:
        for doc in docs_pt:
            idx_content += f"- [{escape_markdown(doc['title'])}]({doc['url']})\n"

    if write_if_changed(INDEX_FILE, idx_content):
        print(f"Generated {INDEX_FILE} with {len(docs_pt)} docs.")

    # Generate EN Index (if translations exist)
    if docs_en:
        idx_en_content = "---\n"
        idx_en_content += "title: Vectora Documentation\n"
        idx_en_content += "---\n\n"
        idx_en_content += "{{< lang-toggle >}}\n\n"

        for doc in docs_en:
            idx_en_content += f"- [{escape_markdown(doc['title'])}]({doc['url']})\n"

        if write_if_changed(INDEX_FILE_EN, idx_en_content):
            print(f"Generated {INDEX_FILE_EN} with {len(docs_en)} docs.")


if __name__ == "__main__":
    main()
