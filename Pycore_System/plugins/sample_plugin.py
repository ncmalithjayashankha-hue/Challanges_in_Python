from utils.colors import print_success, print_info

def hello_cmd():
    print_success("Hello from plugin 🎉")

def register(commands: dict):
    commands["hello"] = {
        "func": hello_cmd,
        "roles": ["admin", "user"]  # allowed roles
    }
    print_info("Sample plugin loaded: hello")