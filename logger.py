from abc import ABC, abstractmethod

class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class FileLogger(Logger):
    def log(self, message: str):
        with open('log.txt', 'a') as log_file:
            log_file.write(f'{message}\n')
        print(f"Log registrado em arquivo: {message}")

class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"Log registrado no console: {message}")
