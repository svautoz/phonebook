import phone_entry

def print_entries(lst: list):
    for entry in lst:
        print(
            f'Имя: {entry.get_name()}\nФамилия: {entry.get_surname()}\nТелефон: {entry.get_phones()}\nОписание: {entry.get_desc()}\n'            
        )

def read_from_csv_file(file):
    phone_entries = []
    for row in file:
        row = row.split(';') 
        phone_entries.append(phone_entry.PhoneEntry(row[3], row[2], row[1], row[0]))
    print_entries(phone_entries)

def read_from_txt_file(file):
    phone_entries = []
    str = file.read()
    str = str.split('\n\n')
    for row in str:
        if len(row) == 0:
            break
        row = row.split('\n') 
        phone_entries.append(phone_entry.PhoneEntry(row[3], row[2], row[1], row[0]))
    print_entries(phone_entries)

def get_data(format):
    entry = phone_entry.PhoneEntry()
    entry.set_name(input('Введите имя:'))
    entry.set_surname(input('Введите фамилию:'))
    entry.set_phones(input('Введите телефон:'))
    entry.set_desc(input('Введите описание:'))

    if format == 'csv':
        str = f'{entry.get_name()};{entry.get_surname()};{entry.get_phones()};{entry.get_desc()};\n'
    if format == 'txt':
        str = f'{entry.get_name()}\n{entry.get_surname()}\n{entry.get_phones()}\n{entry.get_desc()}\n\n'
    return str
    