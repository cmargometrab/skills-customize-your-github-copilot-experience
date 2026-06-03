import sqlite3
from sqlite3 import Connection
from typing import Optional, List, Tuple

DB_FILENAME = "items.db"

def get_connection(db_name: str = DB_FILENAME) -> Connection:
    return sqlite3.connect(db_name)

def create_table(conn: Connection) -> None:
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
        """
    )
    conn.commit()

def add_item(conn: Connection, name: str, quantity: int, price: float) -> int:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)",
        (name, quantity, price),
    )
    conn.commit()
    return cursor.lastrowid

def get_item(conn: Connection, item_id: int) -> Optional[Tuple[int, str, int, float]]:
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, quantity, price FROM items WHERE id = ?", (item_id,))
    return cursor.fetchone()

def list_items(conn: Connection) -> List[Tuple[int, str, int, float]]:
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, quantity, price FROM items")
    return cursor.fetchall()

def update_item(conn: Connection, item_id: int, name: str, quantity: int, price: float) -> bool:
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE items SET name = ?, quantity = ?, price = ? WHERE id = ?",
        (name, quantity, price, item_id),
    )
    conn.commit()
    return cursor.rowcount > 0

def delete_item(conn: Connection, item_id: int) -> bool:
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    return cursor.rowcount > 0

if __name__ == "__main__":
    conn = get_connection()
    create_table(conn)
    print("SQLite persistence starter code is ready. Add your own user interaction and validation logic.")
    conn.close()
