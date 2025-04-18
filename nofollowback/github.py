"""
Lightweight wrapper around GitHub REST API
to fetch followers / following lists.

All public endpoints; authentication token is optional.
"""

from __future__ import annotations

from typing import Set, List
import requests


GITHUB_API = "https://api.github.com"
TIMEOUT = 15


class GitHubAPIError(RuntimeError):
    """Raised on non‑200 response from GitHub API."""


def _fetch_all(url: str, headers: dict) -> List[dict]:
    """Fetch paginated GitHub API results following the Link header."""
    results: List[dict] = []
    while url:
        resp = requests.get(url, headers=headers, timeout=TIMEOUT)
        if resp.status_code != 200:
            raise GitHubAPIError(
                f"GitHub API {resp.status_code}: {resp.json().get('message', '')}"
            )
        results.extend(resp.json())
        url = resp.links.get("next", {}).get("url")
    return results


def get_following(user: str, token: str | None = None) -> Set[str]:
    """Return the set of usernames the given user *follows*."""
    url = f"{GITHUB_API}/users/{user}/following?per_page=100"
    headers = _make_headers(token)
    return {item["login"] for item in _fetch_all(url, headers)}


def get_followers(user: str, token: str | None = None) -> Set[str]:
    """Return the set of usernames that *follow* the given user."""
    url = f"{GITHUB_API}/users/{user}/followers?per_page=100"
    headers = _make_headers(token)
    return {item["login"] for item in _fetch_all(url, headers)}


def _make_headers(token: str | None) -> dict:
    """Construct minimal Accept / Authorization headers."""
    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers
