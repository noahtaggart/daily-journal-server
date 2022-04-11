from models import Entry
import sqlite3
import json

def get_all_entries():
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            e.id,
            e.journalEntry,
            e.date,
            e.userId,
            e.moodId
        FROM Entries e """)
        
        entries = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            entry = Entry(row['id'], row['journalEntry'], row['date'], row['userId'], row['moodId'])
            
            entries.append(entry.__dict__)
    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            e.id,
            e.journalEntry,
            e.date,
            e.userId,
            e.moodId
        FROM Entries e
        WHERE e.id = ?
        """, (id, ))
        
        data = db_cursor.fetchone()
        
        entry = Entry(data['id'], data['journalEntry'], data['date'], data['userId'], data['moodId'])
        
    return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute("""
        DELETE FROM entries
        WHERE id = ?
        """, (id, ))
        
def create_entry(new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        INSERT INTO Entries
            (journalEntry, date, userId, moodId)
        VALUES
            (?, ?, ?, ?);
        """, (new_entry['journalEntry'], new_entry['date'],new_entry['userId'], new_entry['moodId'], ))
        
        id = db_cursor.lastrowid
            
            
        new_entry['id'] = id
            
    return json.dumps(new_entry)