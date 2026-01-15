import psutil
import time
import os
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, BarColumn, TextColumn

console = Console()

# Warning Thresholds
CPU_Threshold = 80
MEM_Threshold = 80
DISK_Threshold = 90

#History for sparklines
cpu_history = []
mem_history = []

def clear():
    os.system('clear')

while True:
    clear()
    #CPU
    cpu_usage = psutil.cpu_percent(interval=0.1)
    cpu_history.append(cpu_usage)
    if len(cpu_history) > 20:
        cpu_history.pop(0)

    #Memory
    memory = psutil.virtual_memory()
    memory_precent = memory.percent
    mem_history.append(memory_precent)
    if len(mem_history) > 20:
        mem_history.pop(0)

    #Disks
    disk = psutil.disk_usage('/')
    disk_precent = disk.percent

    #Up time
    uptime_sec = time.time() - psutil.boot_time()
    uptime_hrs = int(uptime_sec//3600)
    uptime_min = int((uptime_sec%3600)//60)
    uptime_sec = int(uptime_sec%60)

    #Running Process
    process_count = len(psutil.pids())

    #Table
    table = Table(title="System Health Monitor")
    table.add_column("Metric", style="bold cyan")
    table.add_column("Usage / Value", style="bold magenta")

    table.add_row("CPU Usage", f"{cpu_usage}% {'WARNING' if cpu_usage > CPU_Threshold else''}")
    table.add_row("MEM Usage", f"{memory_precent}% {'WARNING' if memory_precent > MEM_Threshold else''}")
    table.add_row("Disk Usage", f"{disk_precent}% {'WARNING' if disk_precent > DISK_Threshold else''}")
    table.add_row("System Uptime", f"{uptime_hrs}h:{uptime_min}m:{uptime_sec}s")
    table.add_row("Running Processes", f"{process_count}")

    console.print(table)

    console.print("CPU History")
    with Progress("[progress.percentage] {task.percentage:>3.0f}%", BarColumn(), TextColumn("{task.description}")) as progress:
        task = progress.add_task("CPU", total=100)
        for value in cpu_history:
            progress.update(task,completed=value)
            time.sleep(0.001)

    console.print("Memory History")
    with Progress("[progress.percentage] {task.percentage:>3.0f}%", BarColumn(), TextColumn("{task.description}")) as progress:
        task = progress.add_task("Memory", total=100)
        for value in mem_history:
            progress.update(task,completed=value)
            time.sleep(1)
