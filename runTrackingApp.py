import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

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
        messagebox.showinfo("Run Logged Successfully!", run_data)
    except Exception as e:
        messagebox.showerror("Error", str(e))

    # Clear input
    date_entry.delete(0, tk.END)
    distance_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)
    pace_entry.delete(0, tk.END)

def plot_progress():
    try:
        df = pd.read_csv('run_log.csv', names = ['Date', 'Distance', 'Time', 'Pace'])
        
        
        df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')
        df['Pace'] = pd.to_numeric(df['Pace'], errors='coerce')
        df = df.dropna()
        
        plt.figure()
        plt.plot(df['Date'], df['Pace'], marker='o', linestyle='-', color='b')
        plt.xlabel('Date')
        plt.ylabel('Pace (Minutes)')
        plt.title('Pace Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

    except FileNotFoundError:
        messagebox.showerror("Error", "No data available to plot! Log some runs first.")

# Basic GUI window
root = tk.Tk()
root.title("Run Tracker")

# Labels and entry fields
tk.Label(root, text="Date (YYYY-MM-DD):").pack()
date_entry = tk.Entry(root)
date_entry.pack()

tk.Label(root, text="Distance (in miles):").pack()
distance_entry = tk.Entry(root)
distance_entry.pack()

tk.Label(root, text="Time (HH:MM:SS):").pack()
time_entry = tk.Entry(root)
time_entry.pack()

tk.Label(root, text="Pace (min/mile):").pack()
pace_entry = tk.Entry(root)
pace_entry.pack()

# Log Run button
log_button = tk.Button(root, text="Log Run", command=log_run)
log_button.pack()

#View Progress Button
progress_button = tk.Button(root, text="View Progress", command=plot_progress)
progress_button.pack()

# Run the app
root.mainloop()