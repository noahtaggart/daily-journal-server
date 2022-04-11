class Entry():
    def __init__(self, id, journalEntry, date, userId, moodId):
        self.id = id
        self.journalEntry = journalEntry
        self.date = date
        self.userId = userId
        self.moodId = moodId
        self.mood = None