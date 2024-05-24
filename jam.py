import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    time_label.config(text=current_time)
    root.after(1000, update_time)  

root = tk.Tk()
root.title("Jam Coy")
root.geometry("300x150")
root.configure(bg="black")

time_label = tk.Label(root, text="jhjhjhjhjhjhjhjhjhjjhjhuhjhjhjj", font=("Helvetica", 48), fg="white", bg="#0B666A")
time_label.pack(pady=40)

update_time()  

root.mainloop()

