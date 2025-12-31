from rich.console import Console
import time

console = Console()

def heavy_task():
    time.sleep(6)

with console.status("[bold magenta]Working...[/bold magenta]", spinner="earth"):
    heavy_task()

console.print("[green]✔ Task completed[/green]")
