class Logger:
    def log(message: str):
        with open("error_log.txt", "a") as log_file:
                log_file.write(f"Error: {message}")

class DatabaseWriter:

    def __init__(self, database, logger) -> None:
        self.database = database
        self.logger = logger

    def write(self, record: tuple):
        try:
            self.database.write(record)
        except Exception as e:
            self.logger.log(f"Error: {e}")

## Extendable
class DatabaseWriter:
    def __init__(self, database, logger) -> None:
        self.database = database
        self.logger = logger

    def write(self, record: tuple):
        try:
            self.database.write(record)
        except Exception as e:
            self.logger.log(f"Error: {e}")


database = object()
DatabaseWriter(database, Logger())