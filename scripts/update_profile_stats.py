"""Generate README cards using only public GitHub repository data."""

import json
import os
from collections import Counter
from datetime import datetime, timezone
from html import escape
from pathlib import Path
from urllib.request import Request, urlopen


def fetch(path):
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "Profile-Stats"}
    if token := os.environ.get("GITHUB_TOKEN"):
        headers["Authorization"] = f"Bearer {token}"
    request = Request(f"https://api.github.com{path}", headers=headers)
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def card(title, subtitle, rows):
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="480" height="270" '
        'viewBox="0 0 480 270" role="img">',
        f"<title>{escape(title)}</title>",
        '<rect x="0.5" y="0.5" width="479" height="269" rx="12" '
        'fill="#ffffff" stroke="#d0d7de"/>',
        '<g font-family="Segoe UI,Arial,sans-serif">',
        f'<text x="24" y="36" font-size="19" font-weight="600" '
        f'fill="#2958f7">{escape(title)}</text>',
        f'<text x="24" y="59" font-size="11" fill="#57606a">{escape(subtitle)}</text>',
    ]
    for index, (label, value) in enumerate(rows):
        y = 91 + index * 25
        parts.append(
            f'<text x="24" y="{y}" font-size="13" fill="#24292f">{escape(label)}</text>'
            f'<text x="455" y="{y}" text-anchor="end" font-size="13" '
            f'font-weight="600" fill="#24292f">{escape(str(value))}</text>'
        )
    day = datetime.now(timezone.utc).strftime("%Y-%m-%d UTC")
    parts.append(f'<text x="24" y="250" font-size="10" fill="#57606a">Updated {day} · GitHub public data</text></g></svg>')
    return "\n".join(parts) + "\n"


def main():
    username = os.environ.get("PROFILE_USERNAME", "Quanghoang7743")
    user = fetch(f"/users/{username}")
    repos = []
    page = 1
    while True:
        batch = fetch(f"/users/{username}/repos?type=owner&per_page=100&page={page}")
        repos.extend(repo for repo in batch if not repo.get("private"))
        if len(batch) < 100:
            break
        page += 1
    original = [repo for repo in repos if not repo["fork"]]
    languages = Counter()
    for repo in original:
        if repo["size"]:
            languages.update(fetch(f"/repos/{username}/{repo['name']}/languages"))
    total = sum(languages.values())
    output = Path(__file__).resolve().parents[1] / "profile"
    output.mkdir(exist_ok=True)
    (output / "stats.svg").write_text(card(
        f"{username} · GitHub", "Public repositories and community", [
            ("Public repositories", len(repos)),
            ("Original repositories", len(original)),
            ("Stars on original repositories", sum(repo["stargazers_count"] for repo in original)),
            ("Forks of original repositories", sum(repo["forks_count"] for repo in original)),
            ("Followers", user["followers"]),
            ("Following", user["following"]),
        ]
    ), encoding="utf-8")
    (output / "languages.svg").write_text(card(
        "Most used languages", "Share of code bytes · public non-fork repositories",
        [(name, f"{count / total:.1%}") for name, count in languages.most_common(6)]
        if total else [("No public code found", "—")],
    ), encoding="utf-8")
    print(f"Generated cards from {len(repos)} public repositories; {len(original)} non-forks.")


if __name__ == "__main__":
    main()
