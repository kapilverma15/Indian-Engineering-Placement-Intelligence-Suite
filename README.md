🎓 Indian Engineering Placement Intelligence Suite

An interactive Streamlit-based placement analytics dashboard for analyzing engineering student placement data using Python, Pandas, SQLite, SQL, and Plotly.

The application loads placement data from a CSV file into a local SQLite database and provides interactive filters, executive KPIs, analytical visualizations, future projections, and an ad-hoc SQL query sandbox.

🚀 Project Overview

The Indian Engineering Placement Intelligence Suite is designed to explore relationships between academic performance, technical skills, internships, projects, college tiers, branches, and placement outcomes.

The Streamlit application displays:

Active cohort size

Placement rate

Average package of placed students

Highest package

Interactive placement and compensation visualizations

Skill and competency comparisons

Future package projection analysis

Hiring conversion funnel

Custom SQL query execution

The dashboard is configured with the page title "Placement Intelligence & Analytics Suite" and uses a wide Streamlit layout.

🛠️ Tech Stack

Technology

Purpose

Python

Application and analytics logic

Streamlit

Interactive dashboard UI

Pandas

Data loading, transformation and analysis

NumPy

Numerical processing

SQLite

Local database storage

Plotly Express

Interactive charts

Plotly Graph Objects

Advanced visualizations

SQL

Data querying and analytical calculations

📁 Project Structure

Placement-Intelligence/
│
├── app.py
├── analytics.py
├── database.py
├── campus_db.sqlite
├── indian_engineering_placement_2026.csv
└── README.md

Main Files

app.py

The main Streamlit application. It:

Initializes the SQLite database from the CSV dataset

Creates indexes on important student attributes

Provides sidebar filters

Executes parameterized SQL queries

Calculates executive KPIs

Generates the dashboard visualizations

Provides the SQL sandbox

analytics.py

Contains the future projection and tier-parity analysis function. The compute_future_projections() function queries placed students and analyzes package returns across DSA problem-solving bands and college tiers.

database.py

The analytics module imports run_query from this module. Make sure the file is available when using analytics.py independently.

📊 Data Pipeline

The application follows this general workflow:

CSV Dataset
     ↓
Pandas DataFrame
     ↓
Data Cleaning / Missing Value Handling
     ↓
SQLite Database
     ↓
Indexed students Table
     ↓
Parameterized SQL Filtering
     ↓
Pandas Analysis
     ↓
Plotly Visualizations
     ↓
Streamlit Dashboard

During database initialization, the application:

Checks whether the configured CSV file exists.

Loads the CSV using Pandas.

Fills missing Open_Source_Contributions values with the median when the column exists.

Fills missing LinkedIn Activity Score values with the median when the column exists.

Writes the dataset to the SQLite students table.

Creates indexes for:

College_Tier

Branch

Placement_Status

DSA_Problems_Solved

CGPA

🎛️ Interactive Filters

The dashboard provides the following sidebar filters:

College Tier

Branch

CGPA Range

Minimum DSA Problems Solved

The selected values are used to construct a parameterized SQL filter against the students table.

This produces the active cohort used throughout the dashboard.

📌 Executive KPIs

The dashboard displays four top-level metrics:

Active Cohort Size

Number of students remaining after the selected filters.

Placement Rate

Percentage of filtered students whose Placement_Status is Placed.

Average Package

Average Package_LPA among placed students in the filtered cohort.

Highest Package

Maximum Package_LPA among placed students.

📈 Dashboard Visualizations

The application organizes its analysis into five tabs.

1. 🎯 Core Drivers

Package vs DSA Problems Solved

A scatter plot comparing:

DSA problems solved

Package in LPA

College tier

GitHub contributions, when available

The visualization also provides student-level hover information when the required columns are available.

Placement Probability Matrix

A matrix showing placement percentage across combinations of:

Projects completed

Internships completed

2. 🏛️ Institutional & Branches

Placement Conversion & Package by Branch

Compares branches using:

Placement rate

Average placed package

Package Spread by College Tier

A box plot showing package distributions across:

Tier-1

Tier-2

Tier-3

Student Flow Hierarchy

A sunburst visualization representing:

College Tier
    ↓
Branch
    ↓
Placement Status

The visualization uses CGPA as its value and Package LPA for color.

3. 📈 Skill Benchmarks

Competency Radar

Compares the cohort average with students whose package is ₹20 LPA or higher.

The analysis can include available competency fields such as:

CGPA

DSA Problems Solved

Aptitude Score

Communication Score

Soft Skills Score

CGPA and DSA values are scaled for the radar visualization.

Package Distribution by Branch & Gender

A violin plot shows package distribution across branches and gender for placed students.

Package Frequency & Density

A histogram displays the distribution of starting compensation across placed students, grouped by college tier.

4. 🔮 Future Projections

Skill-Driven Marginal Returns

The dashboard groups DSA problem-solving counts into 100-problem bands and calculates the average package for each band.

It then applies the following projection formula:

Projected Package
= Current Average Package
  × (1 + (DSA Milestone / 1000) × 0.35)

This is a project-defined analytical projection model, not a guarantee of future compensation.

Hiring Conversion Funnel

The funnel tracks students through a sequence of criteria:

Total Candidates
      ↓
CGPA ≥ 7.0
      ↓
Internships ≥ 1
      ↓
DSA ≥ 150
      ↓
Placed Candidates

5. 💻 SQL Sandbox

The dashboard includes an Ad-Hoc SQL Execution Sandbox.

Users can enter SQL queries directly against the SQLite students table.

The default example calculates:

Total students by college tier

Average DSA problems solved

Placement rate

Average package among placed students

Query results are displayed directly in the Streamlit dashboard.

Only execute SQL statements that are appropriate for your local project database.

🔬 Additional Analytics Module

analytics.py contains a separate function:

compute_future_projections()

It retrieves placed students using:

SELECT
    DSA_Problems_Solved,
    Package_LPA,
    College_Tier,
    GitHub_Contributions
FROM students
WHERE Placement_Status = 'Placed';

The function produces two analytical outputs:

DSA Curve

DSA problem counts are grouped into 100-problem intervals and average package values are calculated for each interval.

Tier Parity

Students are divided into three skill bands using DSA problem-solving values:

Foundational

Intermediate

Advanced

The analysis then compares average package values across skill bands and college tiers.

⚙️ Installation

1. Clone or copy the project

Place the project files in a single project directory.

2. Create a virtual environment

python -m venv venv

Windows

venv\Scripts\activate

macOS / Linux

source venv/bin/activate

3. Install dependencies

pip install streamlit pandas numpy plotly

SQLite is included with standard Python installations.

▶️ Run the Dashboard

From the project directory:

streamlit run app.py

Streamlit will start the local application and provide a browser URL.

📂 Dataset Configuration

The current application expects the CSV dataset at the path configured in app.py:

CSV_PATH = r"E:\python sql project 4\Campus Plament python sql\indian_engineering_placement_2026.csv"

For another computer or folder, update CSV_PATH to the actual dataset location.

The SQLite database is configured as:

DB_PATH = "campus_db.sqlite"

The database is created locally in the project working directory when it does not already exist.

🗃️ Important Dataset Columns

The application references fields including:

Student_ID
College_Tier
Branch
CGPA
DSA_Problems_Solved
Package_LPA
Placement_Status
Internships_Count
Projects_Count
GitHub_Contributions
Gender
Aptitude_Score
Communication_Score
Soft_Skills_Score
Open_Source_Contributions
LinkedIn_Activity_Score

The exact available columns should match the CSV dataset used by the application.

🧠 SQL & Analytics Concepts Demonstrated

This project demonstrates practical data analytics concepts including:

SQL filtering

Parameterized SQL queries

SQL aggregation

GROUP BY

ORDER BY

Conditional aggregation

Pandas grouping

Pivot tables

Quantile-based segmentation

Data cleaning

Median-based missing value handling

Data binning

KPI calculation

Interactive dashboards

Data visualization

SQLite indexing

Analytical projections

Funnel analysis

🔐 Data & Query Handling

The dashboard uses parameterized SQL values for the dynamically selected college tiers, branches, CGPA range, and minimum DSA threshold.

The application also creates database indexes on frequently filtered fields to support more efficient querying.

⚠️ Current Project Notes

The CSV path in app.py is currently an absolute Windows path and should be changed when moving the project to another machine.

analytics.py imports run_query from database.py; ensure that this module is available if the analytics module is executed separately.

The future projection calculation is a project-defined mathematical model and should be interpreted as an analytical scenario rather than a guaranteed salary forecast.

The SQL sandbox executes user-entered SQL against the local SQLite database.

The dashboard depends on the expected dataset columns being present.

🎯 Project Purpose

This project demonstrates how Python, SQL, data processing, and interactive visualization can be combined to build a practical placement analytics and decision-support dashboard.

It can be used as a portfolio project to demonstrate skills in:

Python + SQL + Pandas + SQLite + Streamlit + Plotly + Data Analytics
