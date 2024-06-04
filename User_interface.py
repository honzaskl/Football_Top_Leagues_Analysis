import tkinter
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt

# Define a mapping for league codes
league_codes = {
    "Premiere League": "PL",
    "La Liga": "PD",
    "Bundesliga": "BL1",
    "Serie A": "SA",
    "League 1": "FL1"
}

# Classes for each type of visualization
class Plot_Ranking_Progression:
    def __init__(self, season, league_code, team_names):
        self.season = season
        self.league_code = league_code
        self.team_names = team_names
        self.file_path = f'data/{league_code}_{season}.csv'
        self.standings_df = pd.read_csv(self.file_path)
        self.total_matchdays, self.max_position = self.get_league_details()

    def get_league_details(self):
        if self.league_code in ['PD', 'PL', 'SA']:
            return 38, 20
        elif self.league_code in ['BL1', 'FL1']:
            return 34, 18
        else:
            raise ValueError("Unsupported league code")

    def plot_team_rankings(self):
        plt.figure(figsize=(12, 8))
        for team_name in self.team_names:
            team_data = self.standings_df[self.standings_df['team_name'] == team_name]
            if not team_data.empty:
                plt.plot(team_data['matchday'], team_data['position'], marker='o', linestyle='-', linewidth=2, markersize=8, label=team_name)
                for idx, row in team_data.iterrows():
                    plt.annotate(row['position'], (row['matchday'], row['position']), textcoords="offset points", xytext=(0,10), ha='center')
            else:
                print(f"No data found for team {team_name}")
        plt.gca().invert_yaxis()
        plt.title(f"Team rankings throughout the {self.season} season in {self.league_code}")
        plt.xlabel("Matchday")
        plt.ylabel("Position")
        plt.grid(True)
        plt.xticks(range(1, self.total_matchdays + 1))
        plt.yticks(range(1, self.max_position + 1))
        plt.legend(loc='lower right')
        plt.show()

class Plot_Point_Progression:
    def __init__(self, season, league_code, team_names):
        self.season = season
        self.league_code = league_code
        self.team_names = team_names
        self.file_path = f'data/{league_code}_{season}.csv'
        self.standings_df = pd.read_csv(self.file_path)
        self.total_matchdays, self.max_position = self.get_league_details()

    def get_league_details(self):
        if self.league_code in ['PD', 'PL', 'SA']:
            return 38, 20
        elif self.league_code in ['BL1', 'FL1']:
            return 34, 18
        else:
            raise ValueError("Unsupported league code")

    def plot_points_progression(self):
        plt.figure(figsize=(12, 8))
        for team_name in self.team_names:
            team_data = self.standings_df[self.standings_df['team_name'] == team_name]
            if not team_data.empty:
                plt.plot(team_data['matchday'], team_data['points'], marker='o', linestyle='-', linewidth=2, markersize=8, label=team_name)
                for idx, row in team_data.iterrows():
                    plt.annotate(row['points'], (row['matchday'], row['points']), textcoords="offset points", xytext=(0,10), ha='center')
            else:
                print(f"No data found for team {team_name}")
        plt.title(f"Team points progression throughout the {self.season} Season in {self.league_code}")
        plt.xlabel("Matchday")
        plt.ylabel("Points")
        plt.grid(True)
        plt.xticks(range(1, self.total_matchdays + 1))
        plt.legend(loc='lower right')
        plt.show()

class Print_TopScorers:
    def __init__(self, season, league_code):
        self.season = season
        self.league_code = league_code
        self.file_path = f'data/{league_code}_{season}_Topscorers.csv'

    def load_data(self):
        top_scorers_df = pd.read_csv(self.file_path)
        top_scorers_df.index += 1
        return top_scorers_df

    def print_table(self):
        top_scorers_df = self.load_data()
        print(top_scorers_df)

class Plot_Home_Away:
    def __init__(self, league_code, season, team_names):
        self.league_code = league_code
        self.season = season
        self.team_names = team_names
        self.file_path = f'data/{league_code}_{season}_sorted.csv'
        self.total_matchdays = 38 if league_code in ['PL', 'PD', 'SA'] else 34
        self.matches_df = pd.read_csv(self.file_path)

    def process_match_data(self, matches_df):
        home_points = {}
        away_points = {}
        for _, match in matches_df.iterrows():
            home_team = match['homeTeam.name']
            away_team = match['awayTeam.name']
            home_score = match['score.fullTime.home']
            away_score = match['score.fullTime.away']
            if home_score > away_score:
                home_points[home_team] = home_points.get(home_team, 0) + 3
                away_points[away_team] = away_points.get(away_team, 0)
            elif home_score < away_score:
                away_points[away_team] = away_points.get(away_team, 0) + 3
                home_points[home_team] = home_points.get(home_team, 0)
            else:
                home_points[home_team] = home_points.get(home_team, 0) + 1
                away_points[away_team] = away_points.get(away_team, 0) + 1
        return home_points, away_points

    def plot_points_progression(self):
        home_points_progression = {team: [0] for team in self.team_names}
        away_points_progression = {team: [0] for team in self.team_names}
        for matchday in range(1, self.total_matchdays + 1):
            matchday_matches = self.matches_df[self.matches_df['matchday'] == matchday]
            home_points, away_points = self.process_match_data(matchday_matches)
            for team in self.team_names:
                home_points_progression[team].append(home_points_progression[team][-1] + home_points.get(team, 0))
                away_points_progression[team].append(away_points_progression[team][-1] + away_points.get(team, 0))
        plt.figure(figsize=(12, 8))
        for team in self.team_names:
            plt.plot(range(0, self.total_matchdays + 1), home_points_progression[team], marker='o', linestyle='-', linewidth=2, markersize=8, label=f'{team} (Home)')
            for i, txt in enumerate(home_points_progression[team]):
                plt.annotate(txt, (i, home_points_progression[team][i]), textcoords="offset points", xytext=(0,10), ha='center')
        plt.title(f"Point progression at home throughout the {self.season} season in {self.league_code}")
        plt.xlabel("Matchday")
        plt.ylabel("Points")
        plt.grid(True)
        plt.xticks(range(0, self.total_matchdays + 1))
        plt.legend(loc='best')
        plt.show()
        plt.figure(figsize=(12, 8))
        for team in self.team_names:
            plt.plot(range(0, self.total_matchdays + 1), away_points_progression[team], marker='o', linestyle='-', linewidth=2, markersize=8, label=f'{team} (Away)')
            for i, txt in enumerate(away_points_progression[team]):
                plt.annotate(txt, (i, away_points_progression[team][i]), textcoords="offset points", xytext=(0,10), ha='center')
        plt.title(f"Point progression away throughout the {self.season} season in {self.league_code}")
        plt.xlabel("Matchday")
        plt.ylabel("Points")
        plt.grid(True)
        plt.xticks(range(0, self.total_matchdays + 1))
        plt.legend(loc='best')
        plt.show()

# Create the main window
root = tkinter.Tk()
root.title("Football League Selector")

# Create a frame
frame = tkinter.Frame(root)
frame.pack()

# Labels
info_frame = tkinter.LabelFrame(frame, text="Input information")
info_frame.grid(row=0, column=0, padx=20, pady=10)

league_label = tkinter.Label(info_frame, text="Top 5 leagues:")
league_label.grid(row=0, column=0)

season_label = tkinter.Label(info_frame, text="Season:")
season_label.grid(row=0, column=1)

# Combobox for choosing a league
league_combobox = ttk.Combobox(info_frame, values=list(league_codes.keys()))
league_combobox.grid(row=1, column=0)

# Spinbox for choosing a season
season_spinbox = tkinter.Spinbox(info_frame, from_=2020, to=2023)
season_spinbox.grid(row=1, column=1)

# Function that displays second pop-up window and takes names of the teams
def display_teams_window(main_window, teams, league, season):
    teams_window = tkinter.Toplevel(main_window)
    teams_window.title("Select Teams")

    # Frame for teams
    teams_frame = tkinter.Frame(teams_window)
    teams_frame.pack()

    vars = []
    for index, team in enumerate(teams):
        var = tkinter.IntVar()
        cb = tkinter.Checkbutton(teams_frame, text=team, variable=var)
        cb.grid(row=index // 5, column=index % 5, sticky='w')
        vars.append((team, var))

    # Analysis options
    analysis_label = tkinter.Label(teams_window, text="Analysis options", font=('Helvetica', 10, 'bold'))
    analysis_label.pack()

    analysis_frame = tkinter.Frame(teams_window)
    analysis_frame.pack()

    analysis_options = [
        "Team rankings",
        "Team points progression",
        "Top goalscorers",
        "Point progression at Home and Away"
    ]
    analysis_vars = []
    for index, option in enumerate(analysis_options):
        var = tkinter.IntVar()
        cb = tkinter.Checkbutton(analysis_frame, text=option, variable=var)
        cb.grid(row=0, column=index, sticky='w')
        analysis_vars.append((option, var))

    def on_submit():
        selected_teams = [team for team, var in vars if var.get() == 1]
        selected_analysis = [option for option, var in analysis_vars if var.get() == 1]
        if not selected_teams or not selected_analysis:
            messagebox.showerror("Selection Error", "You must choose at least one team and one analysis option.")
        else:
            print("Selected teams:", selected_teams)
            print("Selected analysis:", selected_analysis)
            for analysis in selected_analysis:
                if analysis == "Team rankings":
                    plotter = Plot_Ranking_Progression(season, league, selected_teams)
                    plotter.plot_team_rankings()
                elif analysis == "Team points progression":
                    plotter = Plot_Point_Progression(season, league, selected_teams)
                    plotter.plot_points_progression()
                elif analysis == "Top goalscorers":
                    printer = Print_TopScorers(season, league)
                    printer.print_table()
                elif analysis == "Point progression at Home and Away":
                    plotter = Plot_Home_Away(league, season, selected_teams)
                    plotter.plot_points_progression()
            teams_window.destroy()
            main_window.destroy()

    submit_btn = tkinter.Button(teams_window, text="Show", command=on_submit)
    submit_btn.pack()

# Function that takes outputs from first pop-up window, reads appropriate CSV file, and transfers the data to the second pop-up window
def collect_data():
    global league, season
    league = league_combobox.get()
    season = season_spinbox.get()
    if not league or not season:
        messagebox.showerror("Selection Error", "You must choose both a league and a season.")
    else:
        league_code = league_codes.get(league, "")
        filename = f"data/{league_code}_{season}.csv"
        df = pd.read_csv(filename, usecols=[2])
        teams = df.iloc[:, 0].unique()
        display_teams_window(root, teams, league_code, season)

# A button to collect data
collect_button = tkinter.Button(info_frame, text="Choose", command=collect_data)
collect_button.grid(row=2, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()
