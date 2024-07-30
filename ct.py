import tkinter as tk
from datetime import datetime, timedelta
import time

class CountdownTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")
        self.label = tk.Label(root, text="Enter duration or target date/time:", font=("Helvetica", 16))
        self.label.pack()
        self.entry = tk.Entry(root, width=30, font=("Helvetica", 16))
        self.entry.pack()
        self.button = tk.Button(root, text="Start", command=self.start_timer)
        self.button.pack()
        self.timer_label = tk.Label(root, text="", font=("Helvetica", 24))
        self.timer_label.pack()
        self.alert_label = tk.Label(root, text="", font=("Helvetica", 16))
        self.alert_label.pack()

    def start_timer(self):
        self.button.config(state="disabled")
        self.entry.config(state="disabled")
        try:
            duration = self.entry.get()
            if ":" in duration:
                target_time = datetime.strptime(duration, "%H:%M")
                target_time = target_time.replace(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
                if target_time < datetime.now():
                    target_time += timedelta(days=1)
            else:
                target_time = datetime.now() + timedelta(seconds=int(duration))
            self.countdown(target_time)
        except ValueError:
            self.alert_label.config(text="Invalid input. Please enter a valid duration (e.g. 30) or target date/time (e.g. 14:30).")

    def countdown(self, target_time):
        while target_time > datetime.now():
            remaining_time = target_time - datetime.now()
            hours, remainder = divmod(remaining_time.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            self.timer_label.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
        self.alert_label.config(text="Time's up!")
        self.button.config(state="normal")
        self.entry.config(state="normal")

root = tk.Tk()
app = CountdownTimer(root)
root.mainloop()