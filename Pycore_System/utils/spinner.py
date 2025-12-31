from rich.console import Console
from rich.spinner import Spinner
import time

console = Console()

def loading(task_name = "Processing", seconds = 3):
    spinner = Spinner("dots", text=task_name)
    with console.status(spinner):
        time.sleep(seconds)