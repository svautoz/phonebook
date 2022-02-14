class User:
    def __init__(self, name = '', surname = '') -> None:
        self.name = name
        self.surname = surname

    def set_name(self, name):
        self.name = name

    def set_surname(self, surname):
        self.surname = surname

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname