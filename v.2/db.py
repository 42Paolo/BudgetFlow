import sqlite3

def create_tab():
    conn = sqlite3.connect("database_spese.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS spese (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount INT,
            category TEXT
        )
    """)

    conn.commit()
    conn.close()
    print('Tabella spese Pronta!')


def add_expense(amount: int, category: str):
    conn = sqlite3.connect("database_spese.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO spese (amount, category) VALUES (?, ?)",
        (amount, category)
    )
	
    conn.commit()
    conn.close()

    print('Dato Inserito!')


def see_expenses():
    conn = sqlite3.connect("database_spese.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM spese")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()