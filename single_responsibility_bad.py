class DatabaseWriter:
    def __init__(self, database) -> None:
        self.database = database

    def write(self, record: tuple):
        try:
            self.database.write(record)
        except Exception as e:
            with open("error_log.txt", "a") as log_file:
                log_file.write(f"Error: {e}")