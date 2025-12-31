from rich.console import Console
from cli.commands import (
    help_cmd,
    status_cmd,
    exit_cmd,
    login_cmd,
    logout_cmd,
    adduser_cmd,
    listuser_cmd
)
from utils.colors import print_success, print_info, print_error
from utils.spinner import loading
from core.logger import get_logger
from core.plugin_loader import load_plugin
import core.config as config

logger = get_logger("CLI")
console = Console()

COMMANDS = {
    "help": {"func": help_cmd},
    "status": {"func": status_cmd, "roles": ["admin", "user"]},
    "adduser": {"func": adduser_cmd, "roles": ["admin", "user"]},
    "listuser": {"func": listuser_cmd, "roles": ["admin", "user"]},
    "login": {"func": login_cmd},
    "logout": {"func": logout_cmd, "roles": ["admin", "user"]},
    "exit": {"func": exit_cmd},
}

def start_cli():
    print_info("Welcome to Pycore CLI")
    print_info("Type 'help' to see available commands")

    load_plugin(COMMANDS)

    while True:
        try:
            cmd = input("pycore > ").strip().lower()
            if cmd in COMMANDS:
                command = COMMANDS[cmd]

                # Check role
                if "roles" in command:
                    if not config.current_user:
                        print_error("Login required")
                        continue
                    user_role = config.current_user[2]  # role from DB
                    if user_role not in command["roles"]:
                        print_error("Permission denied")
                        continue

                # Execute
                command["func"]()
            else:
                print_error("Unknown command. Type 'help'")
        except KeyboardInterrupt:
            print_info("\nUse 'exit' to quit")
