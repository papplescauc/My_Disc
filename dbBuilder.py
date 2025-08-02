# standard library
import os

# third-party
import psycopg
from dotenv import load_dotenv

def create_users_table(conn: psycopg.Connection):
    with conn.cursor() as cur:
        cur.execute("""
            -- sql
            CREATE TABLE IF NOT EXISTS users (
                UserID SERIAL PRIMARY KEY,
                UserName VARCHAR(50) UNIQUE NOT NULL,
                Email VARCHAR(100) UNIQUE NOT NULL,
                PasswordHash VARCHAR(255) NOT NULL,
                PDGARating INTEGER
            );
        """)
        conn.commit()

def create_courses_table(conn: psycopg.Connection):
    with conn.cursor() as cur:
        cur.execute("""
            -- sql
            CREATE TABLE IF NOT EXISTS courses (
                CourseID SERIAL PRIMARY KEY,
                CourseName VARCHAR(100) NOT NULL,
                Address VARCHAR(255) NOT NULL,
                HoleCount INTEGER NOT NULL
            );
        """)
        conn.commit()

def create_rounds_table(conn: psycopg.Connection):
    """
    Creats the rounds table in the database.

    Note:
    - RoundDate is of type TIMESTAMP and is timezone unaware.
    """
    with conn.cursor() as cur:
        cur.execute("""
            -- sql
            CREATE TABLE IF NOT EXISTS rounds (
                RoundID SERIAL PRIMARY KEY,
                UserID INTEGER REFERENCES users(UserID),
                CourseID INTEGER REFERENCES courses(CourseID),
                RoundDate TIMESTAMP NOT NULL,
                Score INTEGER NOT NULL
            );
        """)
        conn.commit()

def create_holes_table(conn: psycopg.Connection):
    with conn.cursor() as cur:
        cur.execute("""
            -- sql
            CREATE TABLE IF NOT EXISTS holes (
                HoleID SERIAL PRIMARY KEY,
                CourseID INTEGER REFERENCES courses(CourseID),
                HoleNumber INTEGER NOT NULL,
                Par INTEGER NOT NULL,
                Distance INTEGER NOT NULL
            );
        """)
        conn.commit()

def create_hole_attempts_table(conn: psycopg.Connection):
    with conn.cursor() as cur:
        cur.execute("""
            -- sql
            CREATE TABLE IF NOT EXISTS hole_attempts (
                AttemptID SERIAL PRIMARY KEY,
                RoundID INTEGER REFERENCES rounds(RoundID),
                HoleID INTEGER REFERENCES holes(HoleID),
                Strokes INTEGER NOT NULL
            );
        """)
        conn.commit()

def create_all_tables(conn: psycopg.Connection):
    """
    Creates all necessary tables in the database.
    """
    create_users_table(conn)
    create_courses_table(conn)
    create_rounds_table(conn)
    create_holes_table(conn)
    create_hole_attempts_table(conn)





if __name__ == "__main__":
    load_dotenv()
    with psycopg.connect(f"dbname=mydisc_db user={os.getenv('DB_USER')} password={os.getenv('DB_PASSWORD')}") as conn:
        print('connected to the database')
        create_all_tables(conn)
        print('all tables created successfully')
        conn.close()