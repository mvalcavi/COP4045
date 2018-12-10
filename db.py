import sys
import os
import sqlite3
from contextlib import closing
from objects import Items

conn = None

def connect():
    global conn
    if not conn:
        DB_FILE = "shoppingcartapp.sqlite"

        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row

def close():
    if conn:
        conn.close()
