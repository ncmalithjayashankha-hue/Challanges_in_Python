from rich.console import Console
console = Console()
class Colors:
    SUCCESS = "bold green"
    ERROR = "bold red"
    WARNING = "bold yellow"
    INFO = "bold cyan"

def print_success(msg):
    console.print(msg,style=Colors.SUCCESS)

def print_error(msg):
    console.print(msg,style=Colors.ERROR)

def print_warning(msg):
    console.print(msg,style=Colors.WARNING)

def print_info(msg):
    console.print(msg,style=Colors.INFO)