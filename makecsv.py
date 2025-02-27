from UserCommands import UserCommands
from functions import set_how_long_to_fetch_data

how_long_to_fetch_data = set_how_long_to_fetch_data()

UserCommands(how_long_to_fetch_data).write_csv_file()

