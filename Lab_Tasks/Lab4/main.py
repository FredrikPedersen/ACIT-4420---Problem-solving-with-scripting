from typing import List
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import wmi


def get_windows_processes_and_ids() -> List[str]:
    processes: List[str] = []

    for process in wmi.WMI().Win32_Process():
        if not process.Name == "svchost.exe":   # Windows has a lot of processes called svchost running all the time, filtering those out to get a more interesting print.
            processes.append(process.Name + " " + str(process.ProcessId))

    return processes


def print_alphabetically_to_pdf(max_lines: int, content: List[str]):
    document = canvas.Canvas("lab4.pdf", pagesize=A4)
    bottom_margin: int = 20
    content = sorted(content, reverse=True)

    for i in range(max_lines):
        document.drawString(100, bottom_margin, content[i])  # distance_left_margin, distance_bottom, text
        bottom_margin += 20

    document.save()


print_alphabetically_to_pdf(40, get_windows_processes_and_ids())
