#!/usr/bin/env python3

import csv
import os
from datetime import datetime, date

import click
import pandas as pd

CSV_FILE = "bets.csv"
FIELDS = ["placed_at", "player", "wager_type", "stake", "odds"]


def init_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(FIELDS)


@click.group()
def cli():
    """NBA betting logger"""
    init_csv()


@cli.command()
def add():
    """Log a new bet (interactive)"""

    player = click.prompt("Player name", type=str)
    wager_type = click.prompt("Wager type (points, rebounds, PRA, etc)", type=str)
    stake = click.prompt("Stake ($)", type=float)
    odds = click.prompt("Odds (e.g. -110, +125)", type=int)

    placed_at = datetime.now().isoformat(timespec="minutes")

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            placed_at,
            player.strip(),
            wager_type.lower().strip(),
            stake,
            odds
        ])

    click.echo("✅ Bet logged")


@cli.command()
def today():
    """Show today's bets"""
    df = pd.read_csv(CSV_FILE, parse_dates=["placed_at"])
    today_df = df[df["placed_at"].dt.date == date.today()]

    if today_df.empty:
        click.echo("No bets logged today.")
        return

    click.echo("\n📊 Bets placed today:\n")
    click.echo(today_df.to_string(index=False))


if __name__ == "__main__":
    cli()
