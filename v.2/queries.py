from db import get_connection

def add_expense(amount, category):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO expenses (amount, category) VALUES (%s, %s)",
        (amount, category)
    )

    conn.commit()
    cur.close()
    conn.close()


def get_expenses():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM expenses")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows