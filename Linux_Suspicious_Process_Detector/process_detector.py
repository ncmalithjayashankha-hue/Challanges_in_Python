import psutil
import os
import time
from datetime import datetime



while True:
    os.system("clear")
    print("PID\tName\t\tCPU%\tMEM%\tPATH\t\t\tRISK")


    for proc in psutil.process_iter(['pid', 'name']):
        try:
            risk = 0

            cpu= proc.cpu_percent(interval=0.1)
            mem= round(proc.memory_percent(),2)
            path= proc.exe()
            name= proc.name()

            if cpu>50:
                risk += 30

            if path.startswith(("/temp", "var/temp", "/dev")):
                risk += 40

            if name.startswith("."):
                risk += 20

            if risk>=70:
                alert = "🔴 HIGH"
                with open("threat_report.log", "a") as f:
                    f.write(
                        f"{datetime.now()} | "
                        f"{name} | PID {proc.pid} | "
                        f"CPU {cpu}% | PATH {path} | \n"
                    )
            elif risk>=40:
                alert = "🟡 MED"
            else:
                alert = "🟢 LOW"

            print(
                f"{proc.pid}\t\t"
                f"{name[:8]}\t\t"
                f"{cpu}\t\t"
                f"{round(mem, 2)}\t"
                f"{path[:20]}\t\t"
                f"{risk}\t"
                f"{alert}"
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
        except KeyboardInterrupt:
            print("Good Bye User")
            break
    time.sleep(3)