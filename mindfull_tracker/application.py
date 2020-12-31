import tkinter as tk
import tkinter.ttk as ttk
import time
from tkinter import messagebox
import db_sdk
from meditation import Meditation
from datetime import datetime

class Application(tk.Frame):

    active = True
    temp = None
    
    def __init__(self, parent, *args, **kwargs):

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.grid(column = 0, row = 0)
        self.create_timer()

    def stop_meditating(self):
        self.active = False

        m = Meditation(self.type.get(), 'beka w chuj' )
        db_sdk.add_meditation(m)

    def create_timer(self):
        self.timer_frame = ttk.Frame(self, padding = "5 5 5 5")
        self.timer_frame.grid(column = 0, row = 0, sticky = (tk.N, tk.W, tk.E, tk.S))
        self.type = tk.StringVar()
        self.med_type = ttk.Combobox(self.timer_frame, textvariable = type)
        self.med_type['values'] = ('Walking', 'Sitting')
        self.med_type.state(["readonly"])
        self.med_type.grid(column = 0, row = 0, padx = 5, pady = 5)

        self.hour = tk.StringVar()
        self.minute = tk.StringVar()
        self.second = tk.StringVar()

        self.hour.set("00")
        self.minute.set("00")
        self.second.set("00")

        self.hourEntry = tk.Entry(self.timer_frame, width = 3, textvariable = self.hour)
        self.hourEntry.grid(column = 1, row = 0, padx = 5, pady = 5)

        self.minuteEntry = tk.Entry(self.timer_frame, width = 3, textvariable = self.minute)
        self.minuteEntry.grid(column = 2, row = 0, padx = 5, pady = 5)

        self.secondsEntry = tk.Entry(self.timer_frame, width = 3, textvariable = self.second)
        self.secondsEntry.grid(column = 3, row = 0, padx = 5, pady = 5)

        self.b_start = tk.Button(self.timer_frame, text = "Start", command = self.countdown, width = 15)
        self.b_start.grid(column = 4, row = 0, padx = 5, pady = 5)

        self.b_stop = tk.Button(self.timer_frame, text = "Stop", command = self.stop_meditating, width = 15)
        self.b_stop.grid(column = 5, row = 0, padx = 5, pady = 5)

    def countdown(self):
        try:
            self.temp = int(self.hour.get()) * 3600 + int(self.minute.get()) \
                * 60 + int(self.second.get())
        except:
            print("Please input the right value")

        while self.temp > -1:
            mins, secs = divmod(self.temp, 60)
            hours = 0

            if mins > 60:
                hours, mins = divmod(mins, 60)

            self.hour.set("{0:2d}".format(hours))
            self.minute.set("{0:2d}".format(mins))
            self.second.set("{0:2d}".format(secs))

            self.parent.update()
            time.sleep(1)

            if self.temp == 0 or not self.active:
                self.active = True
                return

            self.temp -= 1


root = tk.Tk()
Application(root)
root.mainloop()
