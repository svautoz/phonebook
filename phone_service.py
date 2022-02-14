import ui

def print_file(path, format):
    with open(path, 'r') as file:
        if format == 'csv':
            ui.read_from_csv_file(file)
        if format == 'txt':
            ui.read_from_txt_file(file)

def add_phone_entry(path, format):    
    with open(path, 'a') as file:
        if format == 'csv':
            file.write(ui.get_data('csv'))
        if format == 'txt':
            file.write(ui.get_data('txt'))