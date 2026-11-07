#!/usr/bin/env python3
"""Copies the policy texts from the app repo (PennyTrail/docs) into this site.

Usage: python3 tools/sync_from_app.py ../PennyTrail/docs

The app repo's docs/PRIVACY_POLICY.md and docs/TERMS_OF_SERVICE.md are the source of truth.
Their "# Title" and "Effective date: ..." lines become front matter (shown in the page header).
"""
import pathlib
import re
import sys

PAGES = [
    ("PRIVACY_POLICY.md", "pista/index.md", "privacy", "../",
     "How Pista handles your data. Most of it never leaves your phone."),
    ("TERMS_OF_SERVICE.md", "pista/terms/index.md", "terms", "../../",
     "The rules for using Pista, its free trial and Pro subscription."),
]


def convert(text: str, nav: str, root: str, lede: str) -> str:
    lines = text.splitlines()
    title = lines[0].lstrip("# ").strip()
    effective = ""
    body = []
    for line in lines[1:]:
        m = re.match(r"^Effective date:\s*(.+)$", line.strip())
        if m and not effective:
            effective = m.group(1).strip()
            continue
        body.append(line)
    front = [
        "---",
        f'title: "{title}"',
        f'eyebrow: "Pista · Legal"',
        f'lede: "{lede}"',
        f'effective: "{effective}"',
        f"nav: {nav}",
        f'root: "{root}"',
        "---",
    ]
    return "\n".join(front) + "\n" + "\n".join(body).lstrip("\n") + "\n"


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = pathlib.Path(sys.argv[1])
    site = pathlib.Path(__file__).resolve().parent.parent
    for name, dest, nav, root, lede in PAGES:
        out = site / dest
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(convert((src / name).read_text(encoding="utf-8"), nav, root, lede), encoding="utf-8")
        print("wrote", out.relative_to(site))


if __name__ == "__main__":
    main()
