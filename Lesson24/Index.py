import sqlite3
from tkinter.tix import INTEGER
connection = sqlite3.connect('example.db')

cursor = connection.cursor()

cursor.execute('''
Create TABLE ''')