"""
NoFollowBack CLI entry point.

Example:
    $ nofollowback <github_username> --token <TOKEN>
"""

from __future__ import annotations

import sys
import click
from .github import get_followers, get_following, GitHubAPIError


@click.command()
@click.argument("username", metavar="<github_username>")
@click.option(
    "--token",
    "-t",
    help="GitHub Personal Access Token (optional, avoids low rate‑limit).",
    envvar="GITHUB_TOKEN",
)
def cli(username: str, token: str | None) -> None:
    """Show accounts that <github_username> follows but do NOT follow back."""
    try:
        click.echo("📡  Fetching data from GitHub ...", err=True)
        following = get_following(username, token)
        followers = get_followers(username, token)
    except GitHubAPIError as exc:
        click.echo(f"❌  {exc}", err=True)
        sys.exit(1)
    except Exception as exc:  # pragma: no cover
        click.echo(f"❌  Unexpected error: {exc}", err=True)
        sys.exit(1)

    non_followers = sorted(following - followers)

    click.echo()
    count = len(non_followers)
    if count == 0:
        click.secho("✅  Everyone you follow follows you back!", fg="green")
        return

    click.secho(f"🚫  Accounts Not Following You Back ({count}):", fg="red", bold=True)
    for login in non_followers:
        click.echo(f" • {login}")


if __name__ == "__main__":
    cli()
