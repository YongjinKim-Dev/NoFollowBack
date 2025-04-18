# NoFollowBack 🕵️‍♀️

A tiny CLI tool to check which GitHub accounts you follow **aren't following you back**.

## Installation

```bash
pip install nofollowback
```

## Usage

Check accounts that don't follow you back:

```bash
nofollowback <github_username>
```

Example:

```bash
$ nofollowback YongjinKim-Dev
🚫 Accounts Not Following You Back (2):
 • alice
 • bob
```

If you encounter GitHub's rate limits or prefer authenticated requests, you can use your GitHub Personal Access Token:

```bash
nofollowback <github_username> --token <your_github_token>
```