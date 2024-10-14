from rich.console import Console
from rich.table import Table


# Create a Console instance
console = Console()


# Create a Table instance
table = Table(title="Instagram Data")


# Add columns to the table
table.add_column("Genre", justify="left", style="cyan", no_wrap=True)
table.add_column("Views", justify="right", style="magenta")
table.add_column("Likes", justify="right", style="green")
table.add_column("AccountFollowers", justify="right", style="yellow")
table.add_column("Rating", justify="right", style="blue")


# Add example data to the table
table.add_row("Sports", "9119", "248", "1554", "7.5")


# Print the table to the console
console.print(table)

