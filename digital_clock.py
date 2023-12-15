from tkinter import *
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_time)

root = Tk()
root.title("Digital Clock")
clock_label = Label(root, text="", font=("Helvetica", 48))
clock_label.pack(padx=20, pady=20)
update_time()

root.mainloop()