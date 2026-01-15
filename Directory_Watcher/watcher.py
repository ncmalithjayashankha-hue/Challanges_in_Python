import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging

path = "chk_dir"

logging.basicConfig(
    filename="activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

class MyHandler(FileSystemEventHandler):
    def log_event(self, event):
        message = f"{event.event_type} -> {path}"
        print(message)
        logging.info(message)

    def on_created(self, event):
        if not event.is_directory:
            self.log_event("CREATED", path)

    def on_modified(self, event):
        if not event.is_directory:
            self.log_event("MODIFIED", event.src)

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"[Deleted] {event.src_path}")



observer = Observer()
handler = MyHandler()


observer.schedule(handler, path, recursive=True)
observer.start()

try:
    while True:
        print("Watching...")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nWatcher Stopped")
    observer.stop()
observer.join()