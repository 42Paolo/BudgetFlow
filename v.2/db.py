import sqlite3

def crea_tabella():
    conn = sqlite3.connect("database_spese.db")
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS spese (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            importo INT,
            categoria TEXT
        )
    """)
    
    conn.commit()
    conn.close()
    print("Tabella pronta!")