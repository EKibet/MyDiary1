entries = []

class DiaryEntry():

    def __init__(self,title, description, date):
        self.title = title
        self.description = description
        self.date = date

    def addEntry(self):
        mock_db = {'title': self.title, 'description': self.description}
        return entries.append(mock_db)
