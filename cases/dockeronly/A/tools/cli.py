import typer

app = typer.Typer(help="Ops tools for the status page.")


@app.command()
def version() -> None:
    """Print the tool version."""
    print("ops-tools 0.4.0")


if __name__ == "__main__":
    app()
