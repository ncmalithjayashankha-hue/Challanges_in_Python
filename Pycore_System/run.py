from core.database import init_db
from cli.main import start_cli
from gui.main import start_gui

if __name__ == "__main__":
    init_db()
    start_cli()