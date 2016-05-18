class Project:

    def __init__(self, id=None, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    def __repr__(self):
        return "%s:%s:%s" % (str(self.id), self.name, self.description)

    def __eq__(self, other):
        return self.name == other.name and self.description == other.description

    def name(self):
        return self.name
