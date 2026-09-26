import os
from urllib.parse import quote_plus

import pandas as pd
from sqlalchemy import create_engine, text

# --- CONFIURE YOUR MYSQL WORKBENCH CREDENTIALS ----
DB_USER = "root"
DB_PASSWORD = "Kaps@123"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "campus_db"
CSV_PATH = r"E:\python sql project 4\Campus Plament python sql\indian_engineering_placement_2026.csv"

ENCODED_PASSWORD = quote_plus(DB_PASSWORD)
DEFAULT_DATABASE_URL = f"mysql+pymysql://{DB_USER}:{ENCODED_PASSWORD}@{DB_HOST}:{DB_PORT}"
DATABASE_URL = f"{DEFAULT_DATABASE_URL}/{DB_NAME}"
engine = create_engine(DATABASE_URL)


def ensure_database() -> None:
    """Create the target database if it does not exist."""
    default_engine = create_engine(DEFAULT_DATABASE_URL)
    with default_engine.connect() as conn:
        conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`"))
    default_engine.dispose()

    global engine
    engine = create_engine(DATABASE_URL)


def init_db(csv_path: str = CSV_PATH):
    """
    Cleans raw CSV data, imputes nulls, and strems into MySQL.
    """
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Source file '{csv_path}' was not found.")

    ensure_database()

    df = pd.read_csv(csv_path)

    # Imute missing values with medians
    if "Open_Source_Contributions" in df.columns:
        df["Open_Source_Contributions"] = df["Open_Source_Contributions"].fillna(
            df["Open_Source_Contributions"]. median()
        )
    if "LinkedIn Activity Score" in df.columns:
        df["LinkedIn_Activity_Score"] = df["LinkedIn_Activity_Score"].fillna(
            df["LinkedIn_Activity_Score"].median()
        )

    # Stream into MySQL
    df.to_sql("students", con=engine, if_exists="replace", index=False)

    # Create indexes in MySQL using a safe prefix length for string columns.
    with engine.connect() as conn:
        conn.execute(text("ALTER TABLE students ADD INDEX idx_tier (College_Tier(50));"))
        conn.execute(text("ALTER TABLE students ADD INDEX idx_branch (Branch(50));"))
        conn.execute(text("ALTER TABLE students ADD INDEX idx_placement (Placement_Status(20));"))
        conn.execute(text("ALTER TABLE students ADD INDEX idx_cgps (CGPA);"))
        conn.execute(text("ALTER TABLE students ADD INDEX idx_dsa (DSA_Problems_Solved);"))
        conn.commit()

    print("Data successfully loaded and indexed in MySQL Workbench!")


def run_query(query:str, params: tuple =()) -> pd.DataFrame:
    """
    Runs queries against MySQL using SQLAlchemy.
    """
    with engine.connect() as conn:
        return pd.read_sql_query(text(query), conn, params=params)
    

if __name__ == "__main__":
    init_db()
  