from models import Entry, Mood
import sqlite3
import json

def get_all_entries():
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.moodId,
            m.label
        FROM Entries e
        Join Moods m
            ON m.id = e.moodId
        """)
        
        entries = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'], row['moodId'])
            
            mood = Mood(row['moodId'], row['label'])
            
            entry.mood = mood.__dict__
            
            
            entries.append(entry.__dict__)
    return json.dumps(entries)

def search_all_entries(searchTerm):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            m.label mood
        FROM Entries e
        Join Moods m
            ON m.id = e.moodId
        WHERE e.entry LIKE ?
        """, ('%' + searchTerm + '%', ))
        
        entries = []
        
        dataset = db_cursor.fetchall()
        
        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['date'], row['mood'])
            
            # mood = Mood(row['moodId'], row['mood'])
            
            # entry.mood = mood.__dict__
            
            
            entries.append(entry.__dict__)
    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.date,
            e.moodId
        FROM Entries e
        WHERE e.id = ?
        """, (id, ))
        
        data = db_cursor.fetchone()
        
        entry = Entry(data['id'], data['concept'], data['entry'], data['date'], data['moodId'])
        

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
            (concept, date, entry, moodId)
        VALUES
            (?, ?, ?, ?);
        """, (new_entry['concept'], new_entry['date'], new_entry['entry'],new_entry['moodId'], ))
        
        id = db_cursor.lastrowid            
            
        new_entry['id'] = id
        
        entryTags = []
        
        for tag in new_entry['tags']:
            db_cursor.execute("""
            INSERT INTO Entrytags
                (entry_id, tag_id)
            VALUES
                (?, ?);
            """, (id, tag))
            
            entryTags.append(tag)
            
    return json.dumps(new_entry)

def update_entry(id, new_entry):
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
            UPDATE Entries
                SET
                    concept = ?,
                    entry = ?,
                    date = ?,
                    moodId = ?
            WHERE id = ?
            """, (new_entry['concept'], new_entry['entry'], new_entry['date'], new_entry['moodId'], id, ))
        
        rows_affected = db_cursor.rowcount
        
    if rows_affected == 0:
        return False
    else:
        return True
