import user

class PhoneEntry(user.User):
    def __init__(self, description = '', phones_list = [], name = '', surname = '') -> None:
        self.desc = description
        if type(phones_list) == list:
            self.phones = phones_list
        else:
            self.phones = [phones_list]
        self.name = name
        self.surname = surname

    def set_desc(self, desc):
        self.desc = desc

    def set_phones(self, phones):
        self.phones = phones

    def get_desc(self):
        return self.desc

    def get_phones(self):
        return self.phones