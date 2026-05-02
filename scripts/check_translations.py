import os


def check_translations(content_dir):
    """
    Checks for missing or outdated English translations for Portuguese files.
    """
    print(f"Checking translations in: {content_dir}\n")

    missing_en = []
    mismatched_lines = []

    for root, dirs, files in os.walk(content_dir):
        for file in files:
            # Process only Portuguese files
            if file.endswith(".pt.md"):
                pt_path = os.path.join(root, file)
                en_file = file.replace(".pt.md", ".en.md")
                en_path = os.path.join(root, en_file)

                # Check if English version exists
                if not os.path.exists(en_path):
                    missing_en.append(pt_path)
                    continue

                # Check line count consistency
                try:
                    with open(pt_path, "r", encoding="utf-8") as f:
                        pt_lines = len(f.readlines())
                    with open(en_path, "r", encoding="utf-8") as f:
                        en_lines = len(f.readlines())

                    if pt_lines != en_lines:
                        mismatched_lines.append(
                            {
                                "pt_path": pt_path,
                                "en_path": en_path,
                                "pt_count": pt_lines,
                                "en_count": en_lines,
                            }
                        )
                except Exception as e:
                    print(f"Error checking {file}: {e}")

    # Report results
    if missing_en:
        print("Missing English Translations (.en.md):")
        for path in missing_en:
            print(f"  - {path}")
        print()

    if mismatched_lines:
        print("Outdated or Mismatched Translations (Line Count Difference):")
        for item in mismatched_lines:
            diff = item["pt_count"] - item["en_count"]
            status = "More lines in PT" if diff > 0 else "More lines in EN"
            print(
                f"  - {item['pt_path']} ({item['pt_count']} lines) vs {item['en_path']} ({item['en_count']} lines) | {status}"
            )
        print()

    if not missing_en and not mismatched_lines:
        print("All translations are up to date and consistent!")
    else:
        print(
            f"Summary: {len(missing_en)} missing, {len(mismatched_lines)} mismatched."
        )


if __name__ == "__main__":
    content_path = os.path.join(os.getcwd(), "docs", "content")
    if os.path.exists(content_path):
        check_translations(content_path)
    else:
        print(f"Error: Directory {content_path} not found.")
