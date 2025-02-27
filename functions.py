from datetime import datetime
import sys

def set_how_long_to_fetch_data():
    try:
        return sys.argv[1]
    except IndexError:
        return input("How long (in seconds) do you want to run the script? ")

def generate_now_datetime_string():
    return datetime.now().strftime('%Y-%m-%d_%Hh%Mm%Ss')

def generate_mpstat_data(how_long_to_fetch_data):
    return get_data_from_system_command("mpstat -P ALL " + how_long_to_fetch_data + " 1")

def write_file(file_name, file_content):
    with open(file_name, 'w') as file:
        file.write(file_content)

"""
generate_now_datetime_string()
generate_mpstat_data()
"""
def write_raw_data(how_long_to_fetch_data):
    file_name = f"./raw_data/{generate_now_datetime_string()}.csv"
    write_file(file_name, generate_mpstat_data(how_long_to_fetch_data))

def get_data_from_system_command(system_command):
    import subprocess
    return subprocess.check_output(system_command, shell=True).decode()
