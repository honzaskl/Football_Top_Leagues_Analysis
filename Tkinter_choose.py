import tkinter
from tkinter import ttk

# Create the main window
root = tkinter.Tk()
root.title("Football League Selector")

#Create a frame
frame = tkinter.Frame(root)
frame.pack()

info_frame = tkinter.LabelFrame(frame, text = "Input information")
info_frame.grid(row = 0, column = 0, padx = 20, pady = 10)

league_label = tkinter.Label(info_frame, text="Top 5 leagues:")
league_label.grid(row=0, column=0)

season_label = tkinter.Label(info_frame, text="Season:")
season_label.grid(row=0, column=1)

league_combobox = ttk.Combobox(info_frame, values=["", "Premiere League", "La Liga", "Bundesliga", "Serie A", "League 1"])
league_combobox.grid(row=1, column=0)

season_spinbox = tkinter.Spinbox(info_frame, from_=2000, to=2024)
season_spinbox.grid(row=1, column=1)

# Function to simulate fetching data
def collect_data():
    league = league_combobox.get()
    season = season_spinbox.get()
    print(f"Collect data for {league}, Season {season}")

# Add a button to fetch data
collect_button = tkinter.Button(info_frame, text="Choose", command=collect_data)
collect_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()