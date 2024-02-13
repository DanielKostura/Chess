import tkinter as tk

class Timer:
    def __init__(self, canvas, min, sec, bonus):
        self.canvas = canvas
        self.time = min*60 + sec
        self.bonus = bonus
        self.formated_time = tk.StringVar()
        self.formated_time.set(self.format_time())
        
        self.time_label = tk.Label(canvas, textvariable=self.formated_time, font=("Arial", 24))
        self.time_label.pack()

        self.button_start = tk.Button(canvas, text="Štart", command=self.start_timer, font=("Arial", 14))
        self.button_start.pack()

        self.button_stop = tk.Button(canvas, text="Stop", command=self.stop_timer, state=tk.DISABLED, font=("Arial", 14))
        self.button_stop.pack()

        self.active_timer = None

    def format_time(self):
        mins = self.time // 60
        secs = self.time % 60
        return f"{mins:02}:{secs:02}"

    def update_time(self):
        if self.time > 0:
            self.time -= 1
            self.formated_time.set(self.format_time())
            self.active_timer = self.canvas.after(1000, self.update_time)
        else:
            self.button_stop.config(state=tk.DISABLED)
            self.button_start.config(state=tk.NORMAL)

    def start_timer(self):
        self.update_time()
        self.button_start.config(state=tk.DISABLED)
        self.button_stop.config(state=tk.NORMAL)

    def stop_timer(self):
        if self.active_timer is not None:
            self.time += self.bonus
            self.formated_time.set(self.format_time())
            self.canvas.after_cancel(self.active_timer)
            self.button_stop.config(state=tk.DISABLED)
            self.button_start.config(state=tk.NORMAL)

if __name__ == "__main__":
    canvas = tk.Tk()
    canvas.title("Časovač")
    canvas.geometry("250x150")
    timer = Timer(canvas, 0, 10, 3)
    canvas.mainloop()


