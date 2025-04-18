# NoFollowBack 🕵️‍♀️

A tiny CLI that shows which GitHub accounts **you follow but don't follow you back**.

```bash
$ nofollowback <github_username>
🚫 Accounts Not Following You Back (2):
 • torvalds
 • rust-lang
```

## Installation

```bash
pip install nofollowback
```

## Usage

```bash
nofollowback <github_username> [--token YOUR_GH_TOKEN]
```

Token is optional but recommended to avoid GitHub’s low unauthenticated rate‑limit.
