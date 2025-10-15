
from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self):
        pass

class TextLogger(Logger):
    def log(self):
        print("Opening Text File -> Writing Log -> Closing the Text File")

class JSONLogger(Logger):
    def log(self):
        print("Opening JSON File -> Writing Log in JSON format -> Closing JSON File")

class ConsoleLogger(Logger):
    def log(self):
        print("Logging to Console")


class LoggerFactory:
    def get_logger_to_log(self, log_type: str) -> Logger:
        if log_type == "text":
            return TextLogger()
        elif log_type == "json":
            return JSONLogger()
        elif log_type == "console":
            return ConsoleLogger()
        else:
            raise ValueError(f"Unknown logger type: {log_type}")

if __name__ == "__main__":
    logger_type = input("Enter the Logger Type you want to Log into:")
    logger = LoggerFactory()
    logger_instance = logger.get_logger_to_log(logger_type)
    logger_instance.log()




