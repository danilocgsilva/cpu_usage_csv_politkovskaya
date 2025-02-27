from functions import write_raw_data

class UserCommands:
    def __init__(self, how_long_to_fetch_data):
        self.how_long_to_fetch_data = how_long_to_fetch_data

    def write_csv_file(self):
        write_raw_data(self.how_long_to_fetch_data)
