from datetime import datetime

def generate_now_datetime_string():
    return datetime.now().strftime('%Y-%m-%d_%Hh%Mm%Ss')

def create_file(raw_data_file_path):
    with open(raw_data_file_path, 'w') as file:
        file.write(get_system_data() + '\n')

def get_system_data():
    return "abc1234"
