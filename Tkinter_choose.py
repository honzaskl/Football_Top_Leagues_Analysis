import tkinter
from tkinter import ttk
import pandas as pd

# Define a mapping for league codes
league_codes = {
    "Premiere League": "PL",
    "La Liga": "PD",
    "Bundesliga": "BL1",
    "Serie A": "SA",
    "League 1": "FL1"
}

# Create the main window
root = tkinter.Tk()
root.title("Football League Selector")

# Create a frame
frame = tkinter.Frame(root)
frame.pack()

#lables
info_frame = tkinter.LabelFrame(frame, text="Input information")
info_frame.grid(row=0, column=0, padx=20, pady=10)

league_label = tkinter.Label(info_frame, text="Top 5 leagues:")
league_label.grid(row=0, column=0)

season_label = tkinter.Label(info_frame, text="Season:")
season_label.grid(row=0, column=1)

#combobox for choosing a league
league_combobox = ttk.Combobox(info_frame, values=list(league_codes.keys()))
league_combobox.grid(row=1, column=0)

#spinbox for choosing a season
season_spinbox = tkinter.Spinbox(info_frame, from_=2020, to=2023)
season_spinbox.grid(row=1, column=1)

#function that displays second pop-up window and takes names of the teams 
def display_teams_window(teams):
    teams_window = tkinter.Toplevel(root)
    teams_window.title("Select Teams")
    vars = []
    for team in teams:
        var = tkinter.IntVar()
        cb = tkinter.Checkbutton(teams_window, text=team, variable=var)
        cb.pack()
        vars.append((team, var))
    def on_submit():
        selected_teams = [team for team, var in vars if var.get() == 1]
        print("Selected teams:", selected_teams)
    submit_btn = tkinter.Button(teams_window, text="Show", command=on_submit)
    submit_btn.pack()

#function that takes outputs from first pop-up window, read appropriate CSV file and transfer the data in the second pop-up window
def collect_data():
    league = league_combobox.get()
    season = season_spinbox.get()
    league_code = league_codes.get(league, "")
    filename = f"data/{league_code}_{season}.csv"
    df = pd.read_csv(filename, usecols=[2])
    teams = df.iloc[:, 0].unique()
    display_teams_window(teams)

# A button to coolect data
collect_button = tkinter.Button(info_frame, text="Choose", command=collect_data)
collect_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()