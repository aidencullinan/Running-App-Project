import tkinter as tk
from tkinter import messagebox
import pandas as pd

def log_run():
    date = date_entry.get()
    distance = distance_entry.get()
    time = time_entry.get()
    pace = pace_entry.get()

    # Save the run data in a CSV file using Pandas
    run_data = {'Date': date, 'Distance': distance, 'Time': time, 'Pace': pace}
    df = pd.DataFrame([run_data])

    try:
        df.to_csv('run_log.csv', mode='a', header=False, index=False)
        messagebox.showinfo("Success", "Run logged successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

    # Clear input fields
    date_entry.delete(0, tk.END)
    distance_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    pace_entry.delete(0, tk.END)

# Basic GUI window
root = tk.Tk()
root.title("Run Tracker")
root.frame

# Labels and entry fields
tk.Label(root, text="Date (YYYY-MM-DD):").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Distance (in miles):").pack()
distance_entry = tk.Entry(root)
distance_entry.pack()

tk.Label(root, text="Time (in minutes):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Label(root, text="Pace (min/mile):").pack()
pace_entry = tk.Entry(root)
pace_entry.pack()

# Log Run button
log_button = tk.Button(root, text="Log Run", command=log_run)
log_button.pack()

# Run the app
root.mainloop()