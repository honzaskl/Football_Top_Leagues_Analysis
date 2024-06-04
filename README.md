# Project Football-top-leagues-analysis
Welcome to our Python project for “Data Processing in Python” (JEM207) aimed at analyzing the performances of football teams in top 5 leagues in Europe across various seasons, including dynamic progressions and top scorers. We prepared a module that allows users to choose the individual league and season. Next, user has a possibility to choose several teams involved in that particular league and season and further type of analysis desired. The module will take into account all the inputs and either in a form of a graphic visualisation or a table it will display the progressive performance of the desired teams in terms of rank position, season points collection and the division of performaces at a home court and away.

The ultimate goal is to provide a deeper analysis of football leagues that is not given right away and could serve for personal use as well as giving you a more thorough understanding of the particular seasons went. Hopefully it will meet user's requirements a we wish you all the joy with our project.

The authors: Jakub Čakan, Jan Sklenička

## How to run the project on your device?
1. Have installed Git on your device. You can download it using the following link: https://git-scm.com/downloads. Also, have Python installed. (versions >=3.7 are compatible with the project.)

2. Start by cloning the project repository on your machine. Open command prompt or terminal (press the windows button on your keyboard and search for "terminal" or use "command + t" for macOS). Set your desired current working directory using the following command (replace "file_path" with your path in a similar form as "C:/Users/mypersonal/Desktop...", CAREFUL if you copy that directly from your File Explorer, you need to rewrite the backslashes "\" to "/"):
<pre>
cd file_path
</pre>
Press enter to execute. To clone the repository use the following command and execute.
<pre>
git clone https://github.com/honzaskl/Project_football_top_leagues_analysis.git
</pre>

3. To open the project, go to the file where you cloned the repository (it should be your "file_path" from step two) using the following command for example.
<pre>
cd Project_football_top_leagues_analysis
</pre>

4. Install all required libraries specified in the "requirements.txt" using the following command. After this step, you should be able to run all the files without any other issues. 
<pre>
pip install -r requirements.txt
</pre>

5. To open the user interface, please run the file "User-interface.py" (you can find it in the "Running Python" folder) using your preferred code editor/runner (for example Virtual Studio Code - https://code.visualstudio.com/download). 

6. Further proceed as described in the following section "How does user interface work?". 

## How does the user interface work?
We have created a simple modern-looking graphical user interface (GUI) for your simplicity and comfortability. Initially, users are presented with a primary pop-up window where they can select from one of five major European leagues—Premier League (England), Bundesliga (Germany), Ligue 1 (France), Serie A (Italy), and La Liga (Spain). Alongside the league selection, users can choose a specific season, ranging from 2020/21 to 2023/24 (seasons however represented by the initial year). This customization allows users to tailor their analysis to specific leagues and timeframes, making the tool both versatile and powerful.

Once the league and season are selected, the interface triggers a second pop-up window that dynamically retrieves and displays the teams participating in the chosen league and season from a corresponding CSV file, ensuring the user choosing according to the proper listings. In this second window, users can select one or more teams to analyze further (at least one is required). After selecting the teams, users are then prompted to choose the type of analysis they wish to view: season rank progression, points in a season progression, and points progression on home and away grounds, as well as a table of top scorers. Each of these analytical options provides valuable insights, catering to different aspects of football performance and achievements. Again, choice of at least one analytical option is required.

Following the submussion, the user can simply enjoy the graphical visualisation and informative tables to enhance the knowledge in top football environment.

## About the data sources
Our data is sourced from the robust football database available at https://api.football-data.org. This API is renowned for its comprehensive and up-to-date football statistics, covering a wide range of leagues, teams, players, and matches. To ensure that our application runs smoothly and efficiently, we pre-downloaded all relevant data and stored it in a dedicated directory named "data". This data storage strategy not only enhances the application's performance but also eliminates the dependency on real-time data fetching, making the analysis process seamless and uninterrupted. 

The stored data is organized into individual files to facilitate easy and quick data retrieval based on user selections. Each file follows a specific naming convention to aid in identifying the required dataset accurately. For example, files related to general season rank or points obtained are named using the format "short-league-name_season.csv". In contrast, files containing data for top goal scorers are named "short-league-name_season_Topscorers.csv", and those detailing home and away points progression use the format "short-league-name_season_sorted.csv". This structured approach ensures that when a user selects a particular analysis option, the system can efficiently reference the appropriate file, thus providing the requested insights promptly. Whether analyzing overall season rankings, points progression, or identifying top scorers, our organized data repository ensures that all analyses are accurate and readily accessible.

Additionally, the script used to download all the files from the API is contained within a Jupyter Notebook file named "IES_python.ipynb". This file includes the Python code necessary for fetching and storing the comprehensive football data used in our analysis tool. 

## Graphics
Based on the previous analysis we provide a graphical visualization for you. All consecutive matches are visually represented to ensure continuity, with different teams distinctly color-coded in the graphs. This approach makes the graphs both clear and visually appealing, allowing users to easily track trends and differentiate between teams. 

## Final words
In conclusion, we have made every effort to ensure our code is easy to run and user-friendly. However, due to restrictions on the API, we were unable to utilize all the data we wanted. We have worked diligently to anticipate and cover all possible errors that could arise. We welcome your feedback and look forward to hearing your thoughts. Thank you and have fun!

Jakub Č. & Jan S. 