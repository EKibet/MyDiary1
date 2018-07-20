
"""A 'mock' of the db"""
entries_collection = [{
    'description': u'The chain that has no end',
    'date': '10/10/2018',
    },
    {
    'description': u'meet with group members to agree on project delivery',
    'date': '10/10/2018',
    }
]

class EntryList:

    def __init__(self, description, date):
        """
        defines properties for the objects.
        """
        self.description = description
        self.date = date

    def create(self):
        ''''creates a new instance and stores it in entry_var'''

        entry_var = {"Description": self.description, "Date: self.date": self.date}
        return entries_collection.append(entry_var)