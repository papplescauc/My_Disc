import psycopg

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




if __name__ == "__main__":
    pass