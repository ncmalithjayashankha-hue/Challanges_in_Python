import os
import stat
import time
import hashlib
import argparse
import json
import logging
from rich.console import Console
from rich.text import Text
console = Console()

logging.basicConfig(
    filename = "fim.log",
    level= logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def alert_modified(file):
    console.print(f"[bold yellow] [!] Modified[/] : {file}")

def alert_deleted(file):
    console.print(f"[bold red] [!] Deleted[/] : {file}")

def alert_new(file):
    console.print(f"[bold green] [!] New[/] : {file}")

def scan_directory(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)

            meta = get_file_info(full_path)
            file_hash = calculate_hash(full_path)

            print(f"\nFILE: {full_path}\n")
            print(f"META: {meta}")
            print(f"HASH: {file_hash}\n")

def get_file_info(path):
    info = os.stat(path)

    return {
        "size": info.st_size,
        "permission": stat.filemode(info.st_mode),
        "modified": time.ctime(info.st_mtime),
    }

def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                sha256.update(chunk)
        return sha256.hexdigest()
    except PermissionError:
        return "Permission Denied"

def create_baseline(path, output_file="baseline.json"):
    baseline = {}

    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)

            baseline[full_path] = {
                **get_file_info(full_path),
                "hash": calculate_hash(full_path)
            }

    with open(output_file, "w") as f:
        json.dump(baseline, f, indent=4)

    print(f"[+] Baseline Saved to {output_file}")

def load_baseline(file = "baseline.json"):
    with open(file, "r") as f:
        return json.load(f)

def check_integrity(path, baseline_file="baseline.json"):
    baseline = load_baseline(baseline_file)
    current_files = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)

            current_files[full_path] = {
                **get_file_info(full_path),
                "hash": calculate_hash(full_path)
            }

    for file in baseline:
        if file in current_files:
            if baseline[file]["hash"] != current_files[file]["hash"]:
                # Modified
                console.print(f"[bold yellow][!] MODIFIED[/] {file}")
                logging.warning(f"MODIFIED: {file}")
        else:
            console.print(f"[bold red][!] DELETED[/] {file}")
            logging.error(f"DELETED: {file}")

    for file in current_files:
        if file not in baseline:
            console.print(f"[bold green][+] NEW FILE[/] {file}")
            logging.info(f"NEW FILE: {file}")

def main():
    parser = argparse.ArgumentParser(
        description="Python File Integrity Monitoring System"
    )

    parser.add_argument(
        "action",
        choices=["init","scan"],
        help="init = create baseline | scan = check integrity",
    )

    parser.add_argument(
        "path",
        help="Directory to monitor"
    )

    args = parser.parse_args()
    if args.action == "init":
        create_baseline(args.path)
    elif args.action == "scan":
        check_integrity(args.path)

if __name__ == "__main__":
    main()