Run Tracker
This is a simple Python-based desktop application to log your running data (date, distance, time, pace) using a graphical user interface (GUI) built with Tkinter. The app allows users to enter their run information and saves it in a CSV file for later reference.

Features
Input Fields: Enter the date, distance (in miles), time (in minutes), and pace (minutes per mile) of your run.
Data Storage: The run data is saved in a CSV file (run_log.csv) for easy access and tracking.

Success/Error Feedback: Provides confirmation messages for successful logging or error messages if something goes wrong.
Clears Input Fields: Automatically clears input fields after logging the data.
Future Features
View Logged Runs: A feature to display previously logged runs in the app.
Progress Tracking: Visualize run data (pace over time, distance trends) with graphs.
Run Recommendations: Suggest optimal future runs based on logged data (e.g., gradually increasing distance or improving pace).
Goal Tracking: Set and track running goals.
Requirements
Python 3.x
Tkinter: The standard Python library for creating GUI applications.
Pandas: For handling and saving run data in CSV format.
Install with:
bash
Copy code
pip install pandas
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/aidencullinan/running-app-project.git
Navigate to the project directory:

bash
Copy code
cd run-tracker
Install required dependencies:

bash
Copy code
pip install pandas
Run the application:

bash
Copy code
python runTrackingApp.py
Usage
Open the app.
Enter the Date in YYYY-MM-DD format.
Enter the Distance (in miles).
Enter the Time (in minutes).
Enter the Pace (in minutes per mile).
Click the Log Run button to save the data.
Check the run_log.csv file to see your logged runs.
File Structure
graphql
Copy code
running-app-project/
│
├── runTrackingApp.py      # The main Python file containing the application code
├── run_log.csv            # The CSV file where run data is stored (automatically created)
├── README.md              # This file
